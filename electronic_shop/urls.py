"""electronic_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from api.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('api/v1/categories/', CategoriesAPIView.as_view()),
    # path('api/v1/brand/', BrandAPIView.as_view()),
    # path('api/v1/color/', ColorAPIView.as_view()),
    # path('api/v1/filter_price/', Filter_PriceAPIView.as_view()),
    # path('api/v1/product', ProductAPIView.as_view()),
    # path('api/v1/images/', ImagesAPIView.as_view()),
    # path('api/v1/tag/', TagAPIView.as_view()),
    # path('api/v1/contact_us/', Contact_usAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('', views.HOME, name='home'),
    path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', views.obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('api.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('base/', views.BASE, name='base'),
    path('products/', views.PRODUCT, name='products'),
    path('product_details/<str:id>',
         views.PRODUCT_DETAIL_PAGE, name='product_detail'),
    path('search/', views.SEARCH, name='search'),
    path('contact/', views.Contact_Page, name='contact'),
    path('register/', views.HandleRegister, name='register'),
    path('login/', views.HandleLogin, name='login'),
    path('logout/', views.HandleLogout, name='logout'),
    # Cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/', views.cart_detail, name='cart_detail'),
    path('cart/checkout/', views.Check_out, name='checkout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
