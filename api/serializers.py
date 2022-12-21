from dataclasses import field, fields
from rest_framework import serializers
from el_shops.models import *


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class CategoriesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name',)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name',)


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name',)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name', 'color',)


class Filter_PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter_Price
        fields = ('id', 'price',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('unique_id', 'image', 'name',
        #           'price', 'condition', 'information', 'description', 'stock', 'status', 'create_date')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializer()

    class Meta:
        model = OrderProduct
        fields = "__all__"


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:

        model = Images
        fields = ('id', 'image', 'product',)


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'product',)


class Contact_usSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_us
        fields = ('id', 'name', 'email', 'subject', 'message', 'date',)
