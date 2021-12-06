from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop, name='shop_page'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('product/<int:product_id>', views.product, name='product'),
]
