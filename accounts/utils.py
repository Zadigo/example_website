import hashlib
import secrets
from hashlib import md5
from django.conf import settings


def avatar_dir(instance, filename):
    _, extension = filename.split('.')
    new_file_name = f'{secrets.token_hex(5)}.{extension}'
    return f'avatars/user_{instance.myuser.id}/{new_file_name}'


class BlackMails:
    """
    A mixin that implements functionnalities for barring
    certain types of emails from signing up on the website
    """
    black_mails = ['yopmail']
    non_work_domains = ['gmail', 'outlook', 'live', 'yahoo']

    def __init__(self):
        self.blackmails.extend(getattr(settings, 'BLACKMAILS', []))

    def has_authorized_email(self, email, form=None):
        _, domain = email.split('@')
        if self.blackmails and domain in self.blackmails:
            return False
        if form is not None:
            form.add_error('email', 'Email is not authorized')
        return True
