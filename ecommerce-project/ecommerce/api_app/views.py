from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework.decorators import api_view
from ecommerce_app.models import *
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def product_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

@api_view(['GET', 'PUT', 'DELETE'])
def each_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# @api_view(['GET'])
# def products_list(request):
#     product = Product.objects.all()
#     serializer = ProductSerializer(product, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def product(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)