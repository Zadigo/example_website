from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class HeroSitemap(Sitemap):
    priority = '0.5'
    changefreq = 'monthly'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


HOME_SITEMAPS = {
    'HeroSitemap': HeroSitemap
}
