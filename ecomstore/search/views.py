import re

from django.core.cache import cache
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.shortcuts import render

from ecomstore import settings
from ecomstore.catalog.models import Brand, Category, Product
from ecomstore.search import search
from ecomstore.settings import CACHE_TIMEOUT


COMBO_KEYWORDS = (
    'combo',
    'bundle',
    'kit',
    'package',
    'with battery',
    'with batteries',
    'with charger',
    'charger bundle',
)


def _normalize_product_token(value):
    """Normalize model/search tokens so EDC-27, EDC 27, and EDC27 compare well."""
    return re.sub(r'[^A-Z0-9]+', '', str(value or '').upper())


def _product_text(product):
    return ' '.join([
        str(getattr(product, 'name', '') or ''),
        str(getattr(product, 'slug', '') or ''),
        str(getattr(product, 'meta_description', '') or ''),
        str(getattr(product, 'modelNumber', '') or ''),
        str(getattr(product, 'sku', '') or ''),
    ]).lower()


def _looks_like_combo(product):
    if getattr(product, 'is_combo', False):
        return True
    text = _product_text(product)
    return any(keyword in text for keyword in COMBO_KEYWORDS)


def _matches_query_token(product, query_token):
    if not query_token:
        return False
    values = [
        getattr(product, 'modelNumber', ''),
        getattr(product, 'sku', ''),
        getattr(product, 'name', ''),
        getattr(product, 'slug', ''),
        getattr(product, 'meta_description', ''),
    ]
    return any(query_token in _normalize_product_token(value) for value in values)


def _is_base_model_match(product, query_token):
    """Return True for the standalone/original product, not combo offers."""
    if not query_token or _looks_like_combo(product):
        return False

    model_number = _normalize_product_token(getattr(product, 'modelNumber', ''))
    sku = _normalize_product_token(getattr(product, 'sku', ''))
    name = _normalize_product_token(getattr(product, 'name', ''))

    # Strongest signals first: exact model number or SKU.
    if query_token in (model_number, sku):
        return True

    # Fallback for older products where modelNumber/SKU may be empty.
    return query_token in name


def _base_model_sort_key(product, query_token):
    model_number = _normalize_product_token(getattr(product, 'modelNumber', ''))
    sku = _normalize_product_token(getattr(product, 'sku', ''))
    name = _normalize_product_token(getattr(product, 'name', ''))

    if model_number == query_token:
        rank = 0
    elif sku == query_token:
        rank = 1
    elif name.startswith(query_token):
        rank = 2
    elif query_token in name:
        rank = 3
    else:
        rank = 4

    return (rank, getattr(product, 'ranking', 10) or 10, str(getattr(product, 'name', '') or ''))


def _split_model_search_results(products, query):
    """
    For model-number searches like EDC27, show the original product first,
    then combo/bundle offers for the same model, then other matches.
    """
    query_token = _normalize_product_token(query)
    if not query_token:
        return [], [], list(products), False

    primary = []
    combos = []
    others = []
    seen_ids = set()

    for product in products:
        product_id = getattr(product, 'id', None)
        if product_id in seen_ids:
            continue
        seen_ids.add(product_id)

        if _is_base_model_match(product, query_token):
            primary.append(product)
        elif _looks_like_combo(product) and _matches_query_token(product, query_token):
            combos.append(product)
        else:
            others.append(product)

    primary.sort(key=lambda p: _base_model_sort_key(p, query_token))
    combos.sort(key=lambda p: (getattr(p, 'ranking', 10) or 10, str(getattr(p, 'name', '') or '')))

    # Only switch to the grouped layout when it actually improves the result page.
    use_grouped_layout = bool(primary and combos)
    return primary, combos, others, use_grouped_layout


def results(request, template_name="search/results.html"):
    """Display paginated product search results."""
    q = request.GET.get('q', '').strip()

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    matching_qs = search.products(q).get('products', Product.active.none())

    # Load related objects commonly needed by the product-card template.
    try:
        matching_qs = matching_qs.select_related('brand', 'series').prefetch_related(
            'categories',
            'topattributes_set',
        )
    except Exception:
        # Keep search working even if a legacy manager/queryset cannot use the optimization.
        pass

    matching_list = list(matching_qs)
    primary_results, combo_results, other_results, use_grouped_search = _split_model_search_results(matching_list, q)

    if use_grouped_search:
        matching = primary_results + combo_results + other_results
        results = matching
        paginator = None
    else:
        matching = matching_list
        paginator = Paginator(matching, settings.PRODUCTS_PER_PAGE)
        try:
            results = paginator.page(page).object_list
        except (InvalidPage, EmptyPage):
            results = paginator.page(1).object_list

    page_title = 'Search Results for: ' + q

    if getattr(request, 'flavour', None) == 'mobile':
        template_name = 'mobile/home/searchresults.html'

    list_cache_key = 'active_category_link_list'
    active_categories = cache.get(list_cache_key)
    if not active_categories:
        active_categories = Category.active.all().order_by('ranking')
        cache.set(list_cache_key, active_categories, CACHE_TIMEOUT)

    brand_cache_key = 'active_brand_link_list'
    active_brands = cache.get(brand_cache_key)
    if not active_brands:
        active_brands = Brand.active.all().order_by('ranking')
        cache.set(brand_cache_key, active_brands, CACHE_TIMEOUT)

    return render(request, template_name, locals())
