from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render
from rest_framework import viewsets


def home(request):
    return render(request, 'index.html')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
