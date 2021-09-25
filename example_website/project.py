from django.template.context import Context
from django.contrib.sites.shortcuts import get_current_site

class Company:
    def __init__(self, company_name: str = None):
        self.details = {
            'company_name': company_name or 'MyWebsite',
            'emails': {}
        }
        self.context = Context(self.details)
    
def company_context_processor(request):
    company = Company()
    company.details['domain'] = get_current_site(request)
    return company.context.flatten()
