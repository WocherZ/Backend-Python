from django.urls import path

from . import views

urlpatterns = [
    path('', views.user, name='user_page'),
    path('order', views.order, name='user_order'),
    path('cart', views.cart, name='user_cart'),
    path('registration', views.registration, name='registration')
]
