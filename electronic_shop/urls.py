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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Electronics API",
        default_version='v1',
        description="Electronics APIsi",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="qoziyevsharofiddin199805@gmail.com"),
        license=openapi.License(name="Electronics litsenziyasi"),
    ),
    public=True,
    # permission_classes=[permissions.AllowAny, ],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HOME, name='home'),
    path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', views.obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('api/accounts/', include("accounts.urls")),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include('api.urls')),
    path('api/v1/allauth/', include('allauth.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
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
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
