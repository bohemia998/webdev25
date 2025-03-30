from django.urls import path
from .views import product_list, product_detail, category_list, category_detail, category_products

urlpatterns = [
    path('api/products/', product_list, name='product-list'),
    path('api/products/<int:id>/', product_detail, name='product-detail'),
    path('api/categories/', category_list, name='category-list'),
    path('api/categories/<int:id>/', category_detail, name='category-detail'),
    path('api/categories/<int:id>/products/', category_products, name='category-products'),
]
