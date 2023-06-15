from django.urls import path
from products.views import home, product_description, add_to_cart, cart

urlpatterns = [
    # Other URL patterns
    path('', home, name='home'),
    path('product/<int:product_id>/', product_description, name='product_description'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
]
