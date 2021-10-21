from django.utils import timezone

ICONS = [
    ('Facebook', 'facebook-f'),
    ('Instagram', 'instagram'),
    ('Github', 'github')
]


FOOTER = [
    {
        'title': 'Company',
        'links': [
            {
                'title': 'Home',
                'name': 'legal:privacy'
            }
        ]
    },
    {
        'title': 'About us',
        'links': [
            {
                'title': 'Contact us',
                'name': 'legal:privacy'
            },
            {
                'title': 'Press',
                'name': 'legal:privacy'
            },
            {
                'title': 'Careers',
                'name': 'legal:privacy'
            }
        ]
    },
    {
        'title': 'Information',
        'links': [
            {
                'title': 'About us',
                'name': 'legal:about_us'
            },
            {
                'title': 'Terms of service',
                'name': 'legal:terms_of_service'
            },
            {
                'title': 'Privacy policies',
                'name': 'legal:privacy'
            }
        ]
    }
]

CURRENT_DATE = timezone.now()
