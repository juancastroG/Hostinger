from django.urls import path
from . import views

urlpatterns = [
    path('accessories/', views.all_accessories, name='all_accessories'),
    path('cart/', views.cart, name='cart'),
]