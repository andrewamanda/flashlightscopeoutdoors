# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse
from ecomstore.catalog.models import Product, Brand, Category, Department, SubCategory, Series

class DepartmentSitemap(sitemaps.Sitemap):
    priority = 1.0 
    changefreq = 'weekly'

    def items(self):
        return Department.active.all()

    def lastmod(self, obj):
        return obj.updated_at

class SubCategorySitemap(sitemaps.Sitemap):
    priority = 1.0 
    changefreq = 'weekly'

    def items(self):
        return SubCategory.active.all()

    def lastmod(self, obj):
        return obj.updated_at

class CategorySitemap(sitemaps.Sitemap):
    priority = 1.0 
    changefreq = 'weekly'

    def items(self):
        return Category.active.all()

    def lastmod(self, obj):
        return obj.updated_at

class SeriesSitemap(sitemaps.Sitemap):
    priority = 1.0 
    changefreq = 'weekly'

    def items(self):
        return Series.active.all()
    def lastmod(self, obj):
        return obj.updated_at

class BrandSitemap(sitemaps.Sitemap):
    priority = 1.0 
    changefreq = 'weekly'

    def items(self):
        return Brand.active.all()
    def lastmod(self, obj):
        return obj.updated_at

class ProductSitemap(sitemaps.Sitemap):
    priority = 1.0 
    changefreq = 'weekly'

    def items(self):
        return Product.active.all()
    def lastmod(self, obj):
        return obj.updated_at



class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return [
            'nameyourprice',
            'store_policy',
            'return_policy',
            'product_warranty',
            'email_signup',
            'customer_service',
            'testimonial',
            'secure_shopping',
            'savings_channel',
            'free_shipping',
            'privacy',
        ]

    def location(self, item):
        return reverse(item)
