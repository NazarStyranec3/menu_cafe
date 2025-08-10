from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('product/<int:products_id>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/product/<int:product_id>/', views.product_detail, name='product_detail')
]

