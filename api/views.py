from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from el_shops.models import *
from django.db.models import Q
from django.db.models import Sum
from django.db.models import F
import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import requests


@ api_view(['GET', 'POST'])
def order_list(request):

    if request.method == 'GET':
        orders = Order.objects.all()
        orders_serialized = OrderSerializer(orders, many=True).data

        for order in orders_serialized:
            order_products = OrderProduct.objects.filter(order=order["id"])
            order['records'] = OrderProductSerializer(
                order_products, many=True).data
        return Response(orders_serialized)

    elif request.method == 'POST':
        order_data = request.data

        createdUser = User.objects.get(id=order_data['created_by'])
        order = Order.objects.create(created_by=createdUser)
        product = Product.objects.get(id=order_data["records"]["product_id"])

        op = OrderProduct(
            order=order, product=product, quantity=order_data["records"]["quantity"], price=product.price)
        op.save()
        print(op.id)
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
    return Response(OrderSerializer(order).errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):

    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def total_order_product(request):

    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        print(datetime.datetime.strptime(start_date, '%d-%m-%Y'))
        if start_date is None:
            start_date = datetime.date.today()
        else:
            start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')

        if end_date is None:
            end_date = datetime.date.today()
        else:
            end_date = datetime.datetime.strptime(end_date, '%d-%m-%Y')

        order_product_total = OrderProduct.objects.filter(order__created_at__range=(start_date, end_date)).aggregate(
            total=Sum(F('price') * F('quantity'))
        )['total']
        return Response({
            "order_product_total": order_product_total
        })

    elif request.method == 'POST':
        serializer = OrderProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_product_list(request):
    totals = []
    for queryset in OrderProduct.objects.all():
        totals.append({
            "product_id": queryset.product.id,
            "product": queryset.product.name,
            "total": queryset.price * queryset.quantity
        })

    return Response(totals)


@ api_view(['GET', 'POST'])
def orderproduct_list(request):

    if request.method == 'GET':
        orderproduct = OrderProduct.objects.all()
        serializer = OrderProductSerializer(orderproduct, many=True)
        return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET', 'PUT', 'DELETE'])
def orderproduct_detail(request, pk):

    try:
        orderproduct = OrderProduct.objects.get(pk=pk)
    except OrderProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderProductSerializer(orderproduct)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderProductSerializer(orderproduct, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        orderproduct.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@ api_view(['GET', 'POST'])
def product_list(request):

    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class CategoriesViewSet(viewsets.ModelViewSet):

#     serializer_class = CategoriesSerializer
#     queryset = Categories.objects.all()
#     # filter_backends = [DjangoFilterBackend]
#     # permission_classes = [IsOwnerOrReadOnly, ]


# class BrandViewSet(viewsets.ModelViewSet):

#     serializer_class = BrandSerializer
#     queryset = Brand.objects.all()
#     # filter_backends = [DjangoFilterBackend]
#     # permission_classes = [IsOwnerOrReadOnly, ]


# class ColorViewSet(viewsets.ModelViewSet):
#     queryset = Color.objects.all()
#     serializer_class = ColorSerializer
#     # filter_backends = [DjangoFilterBackend]
#     # permission_classes = [IsOwnerOrReadOnly, ]


# class Filter_PriceViewSet(viewsets.ModelViewSet):
#     queryset = Filter_Price.objects.all()
#     serializer_class = Filter_PriceSerializer


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ImagesViewSet(viewsets.ModelViewSet):
#     queryset = Images.objects.all()
#     serializer_class = ImagesSerializer
#     # filter_backends = [DjangoFilterBackend]
#     # permission_classes = [IsOwnerOrReadOnly, ]


# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     # filter_backends = [DjangoFilterBackend]
#     # permission_classes = [IsOwnerOrReadOnly, ]


# class ContactViewSet(viewsets.ModelViewSet):
#     queryset = Contact_us.objects.all()
#     serializer_class = Contact_usSerializer
#     # filter_backends = [DjangoFilterBackend]
#     # permission_classes = [IsOwnerOrReadOnly, ]
