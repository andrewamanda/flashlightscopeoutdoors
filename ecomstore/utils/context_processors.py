from ecomstore import settings
from ecomstore.catalog.models import Category

def ecomstore(request):
    """ context processor for the site templates """
    return {
            'site_name': settings.SITE_NAME,
			'site_url': settings.SITE_URL,
            'meta_keywords': settings.META_KEYWORDS,
            'meta_description': settings.META_DESCRIPTION,
            'analytics_tracking_id': settings.ANALYTICS_TRACKING_ID,
            'DISTRIBUTOR_SITE_DOMAIN': settings.DISTRIBUTOR_SITE_DOMAIN,
            'DISTRIBUTOR_NAME': settings.DISTRIBUTOR_NAME,
			'SUPPORT_PHONE_NUM': settings.SUPPORT_PHONE_NUM,
            'EMAIL_ORDER': settings.EMAIL_ORDER,
            'request': request
            }
