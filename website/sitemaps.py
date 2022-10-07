from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class Static_Sitemap(Sitemap):
    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['index', 'contact_us', 'booking', 'booking_page', 'inner_page']

    def location(self, item):
        return reverse(item)
