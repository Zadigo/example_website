from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class AuthenticationSitemap(Sitemap):
    priority = '0.5'
    changefreq = 'monthly'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)
