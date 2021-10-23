from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class LegalSitemap(Sitemap):
    priority = '0.7'
    changefreq = 'monthly'

    def items(self):
        return ['about_us', 'terms_of_service', 'terms_of_sale', 'privacy']

    def location(self, item):
        return reverse(item)


LEGAL_SITEMAPS = {
    'LegalSitemap': LegalSitemap
}
