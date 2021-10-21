from typing import List

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.context import Context
from django.utils import timezone

from company.utils import CURRENT_DATE, FOOTER, ICONS


class Company(Context):
    def __init__(self, company_name: str = None):
        self.details = {
            'company_name': company_name or 'MyWebsite',
            **getattr(settings, 'ENTERPRISE', {})
        }

        if 'socials' in self.details:
            socials = self.details.get('socials')
            if not isinstance(socials, list):
                raise TypeError('Socials in ENTERPRISE should be a list')
            # self._check_socials(socials)
        self.details['socials'] = self._add_icon(socials)

        super().__init__(self.details)

    @staticmethod
    def _add_icon(socials: List[dict]):
        for social in socials:
            icon = list(filter(lambda x: social['alt'] in x, ICONS))
            if not icon:
                raise ValueError(
                    f"Social is not in the list of socials: {ICONS}")
            social['icon'] = icon[0][-1]
        return socials

    @staticmethod
    def _check_socials(socials: List[dict]):
        should_have_keys = ['alt', 'url']
        for social in socials:
            for key in social.keys():
                if key not in should_have_keys:
                    raise ValueError(
                        'Socials dict should have alt and url only')


def company(request):
    company = Company()
    company.details['domain'] = get_current_site(request)
    company.push(footer=FOOTER, current_date=CURRENT_DATE)
    return company.flatten()
