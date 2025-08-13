from django.urls import path
from . import views

urlpatterns = [
    # Звичайний каталог
    path('', views.catalog, name='catalog'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('category/<int:category_id>/product/<int:product_id>/', views.product_detail, name='product_detail'),

    # Львівський каталог
    path('lviv/', views.lviv_catalog, name='lviv_catalog'),
    path('lviv_category/<int:category_id>/', views.lviv_category_detail, name='lviv_category_detail'),
    path('lviv_category/<int:category_id>/product/<int:product_id>/', views.lviv_product_detail, name='lviv_product_detail'),
]
