from rest_framework import status
from rest_framework.response import Response

def success_response(data: dict={}):
    return Response(data={'state': True, **data})


def fail_response(data: dict={}):
    data = {'state': False, **data}
    return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def server_error_response(data: dict={}):
    data = {'state': False, **data}
    return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def forbidden_response(data: dict={}):
    data = {'state': False, **data}
    return Response(data, status=status.HTTP_403_FORBIDDEN)


def unauthorized_response(data: dict={}):
    data = {'state': False, **data}
    return Response(data, status=status.HTTP_401_UNAUTHORIZED)
