from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    # path('', cart_detail, name='cart_detail'),
    # path('add/<str:product_model>/<int:product_id>/', cart_add, name='cart_add'),
    # path('remove/<str:product_model>/<int:product_id>/', cart_remove, name='cart_remove'),
    path('cart_order_number/', cart_order_number, name='cart_order_number'),
    path('', get_cart, name='cart_detail'),
    path('add_to_cart/<str:product_model>/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:product_model>/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    # path('clear/', clear, name='clear'),
]
