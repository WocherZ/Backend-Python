from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop, name='shop_page'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('add', views.add, name='add_product'),
    path('product/<int:pk>/update/', views.UpdateProduct.as_view(), name='update_product'),
    path('product/<int:pk>/delete', views.DeleteProduct.as_view(), name='delete_product'),

    path('login', views.login, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('private', views.private, name='private_page')
]
