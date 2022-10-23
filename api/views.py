from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from el_shops.models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


# class CategoriesAPIView(APIView):
#     def get(self, request):
#         cats = Categories.objects.all()
#         serializer = CategoriesSerializer(cats, many=True)
#         return Response(serializer.data)
#     # queryset = Categories.objects.all()
#     # serializer_class = CategoriesSerializer

#     def post(self, request):
#         serializer = CategoriesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=201)
#         else:
#             return Response(status=400)

class CategoriesViewSet(viewsets.ModelViewSet):

    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()


class BrandViewSet(viewsets.ModelViewSet):

    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class Filter_PriceViewSet(viewsets.ModelViewSet):
    queryset = Filter_Price.objects.all()
    serializer_class = Filter_PriceSerializer


# class ProductAPIView(APIView):
#     def get(self, request):
#         prod = Product.objects.all()
#         serializer = ProductSerializer(prod, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=201)
#         else:
#             return Response(status=400)


# class ProductDetailAPIView(APIView):
#     def get(self, request, pk):
#         prod = Product.objects.get(id=pk)
#         serializer = ProductDetailSerializer(prod)
#         return Response(serializer.data)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact_us.objects.all()
    serializer_class = Contact_usSerializer
