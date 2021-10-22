def authentication_token_validity(request):
    from rest_framework.authtoken.models import Token

    header = request.headers.get('Authorization', None)
    if header is None:
        return False
    _, value = header.split(' ')

    try:
        token = Token.objects.get(key__iexact=value)
    except:
        token = None
    return all([token.user.is_active, token is not None])
