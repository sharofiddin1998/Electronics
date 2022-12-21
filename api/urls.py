from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from api import views


urlpatterns = [
    path('orders/', views.order_list),
    path('order/<int:pk>/', views.order_detail),
    path('products/', views.product_list),
    path('product/<int:pk>/', views.product_detail),
    path("orderproduct_list/", views.orderproduct_list),
    path('order_product/<int:pk>/', views.orderproduct_detail),
    path('total_order_product/', views.total_order_product),
    path('order_product_list/', views.order_product_list),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
# router = routers.DefaultRouter()
# router.register(r'categories', views.CategoriesViewSet, basename='category')
# router.register(r'brands', views.BrandViewSet, basename='brand')
# router.register(r'colors', views.ColorViewSet, basename='color')
# router.register(r'filter_prices', views.Filter_PriceViewSet,
#                 basename='filter_price')
# router.register(r'images', views.ImagesViewSet, basename='image')
# router.register(r'tags', views.TagViewSet, basename='tag')
# router.register(r'contacts', views.ContactViewSet, basename='contact')
# urlpatterns = router.urls
