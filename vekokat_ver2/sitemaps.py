from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.urls import reverse
from catalog.models import CatalyzatorCategory, AutoCatalog
from cities.models import City

class CatCategorySitemap(Sitemap):
    changefreq='daily'
    priority=0.5

    def items(self):
        return CatalyzatorCategory.objects.all()

class AutoCatalogSitemap(Sitemap):
    changefreq='daily'
    priority=0.5

    def items(self):
        return AutoCatalog.objects.all()

class CitySitemap(Sitemap):
    changefreq='daily'
    priority=0.5

    def items(self):
        return City.objects.all()

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['main-newdesign', 'new-contacts', 'conditions', 'otechcatalog-view', 'importcatalog-view']
    def location(self, item):
        return reverse(item)
