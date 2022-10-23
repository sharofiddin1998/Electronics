from dataclasses import field, fields
from rest_framework import serializers
from el_shops.models import *


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name',)


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


class ColorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name', 'color',)


class Filter_PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter_Price
        fields = ('id', 'price',)


class Filter_PriceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter_Price
        fields = ('id', 'price',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('unique_id', 'image', 'name',
        #           'price', 'condition', 'information', 'description', 'stock', 'status', 'create_date')


class ProductDetailSerializer(serializers.ModelSerializer):
    brand = BrandDetailSerializer(read_only=True, many=True)
    color = ColorDetailSerializer(read_only=True, many=True)
    categories = CategoriesDetailSerializer(read_only=True, many=True)
    filter_price = Filter_PriceDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        # exclude = ('unique_id', 'image', 'name',
        #            'price', 'condition', 'information', 'description', 'stock', 'status', 'create_date')


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        product = ProductDetailSerializer(read_only=True, many=True)
        model = Images
        fields = ('id', 'image', 'product',)


class TagSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Tag
        fields = ('id', 'name', 'product',)


class Contact_usSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_us
        fields = ('id', 'name', 'email', 'subject', 'message', 'date',)
