import json
import os

from django.conf import settings
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from api.serializers import ProductSerializer


class BaseAPIView(APIView):
    @classmethod
    def get_extra_actions(cls):
        return []

# class ProductsExample(ListAPIView):
#     """An API class to return a simple list of products"""
#     def list(self, request):
#         path = os.path.join(settings.MEDIA_ROOT, 'products.json')
#         with open(path, 'r', encoding='utf-8') as f:
#             data = json.load(f)['products']
#         serialized_data = ProductSerializer(data=data, many=True)
#         if serialized_data.is_valid():
#             return Response(data=serialized_data.data, status=200, content_type='application/json')
#         return Response(data={}, status=400, content_type='application/json')
    # @classmethod
    # def get_extra_actions(cls):
    #     return []


class ProductsExample(BaseAPIView):
    """An API class to return a simple list of products"""
    def get(self, request):
        path = os.path.join(settings.MEDIA_ROOT, 'products.json')
        with open(path, 'r', encoding='utf-8') as f:
            data =json.load(f)
        serialized_data = ProductSerializer(data=data['products'], many=True)
        if not serialized_data.is_valid():
            return Response(data=[], content_type='application/json')
        return Response(data=serialized_data.data)

class ProductExample(BaseAPIView):
    """Get a single product"""
    def get(self, request, **kwargs):
        path = os.path.join(settings.MEDIA_ROOT, 'products.json')
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        item = [item for item in data['products'] if item['id'] == int(kwargs['pk'])]
        return Response(data=item, content_type='application/json')

class CreateProductExample(BaseAPIView):
    """Create a product example"""
    def put(self, request, **kwargs):
        try:
            path = os.path.join(settings.MEDIA_ROOT, 'products.json')
            with open(path, 'w+', encoding='utf-8') as f:
                data = json.load(f)
                last_id = int(data['products'][-1]['id'])
                request.data.update({'id': last_id + 1})
                data['products'].append(request.data)
                new_data = {
                    'products': data
                }
                json.dump(new_data, f, indent=4)
            serialized_data = ProductSerializer(data=data['products'], many=True)
        except:
            return Response(data=[], status=400)
        else:
            if not serialized_data.is_valid():
                return Response(data={})
            return Response(data=serialized_data.data)