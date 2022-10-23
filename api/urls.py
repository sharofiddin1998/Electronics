from django.urls import path
from api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoriesViewSet, basename='category')
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'colors', ColorViewSet, basename='color')
router.register(r'filter_prices', Filter_PriceViewSet, basename='filter_price')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'images', ImagesViewSet, basename='image')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'contacts', ContactViewSet, basename='contact')
urlpatterns = router.urls

# urlpatterns = [
#     # path('api/v1/categories/', CategoriesAPIView.as_view()),
#     # path('api/v1/brand/<int:pk>/', BrandAPIView.as_view()),
#     path('api/v1/brand/', BrandAPIView.as_view()),
#     path('api/v1/color/', ColorAPIView.as_view()),
#     path('api/v1/filter_price/', Filter_PriceAPIView.as_view()),
#     path('api/v1/product/<int:pk>/', ProductDetailAPIView.as_view()),
#     path('api/v1/product/', ProductAPIView.as_view()),
#     path('api/v1/images/', ImagesAPIView.as_view()),
#     path('api/v1/tag/', TagAPIView.as_view()),
#     path('api/v1/contact_us/', Contact_usAPIView.as_view()),
# ]
