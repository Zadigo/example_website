import hashlib
import secrets
from hashlib import md5


def avatar_dir(instance, filename):
    _, extension = filename.split('.')
    new_file_name = f'{secrets.token_hex(5)}.{extension}'
    return f'avatars/user_{instance.myuser.id}/{new_file_name}'
