from django.urls import path
from ecommerce import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup_success/', views.signup_success, name='signup_success'),
    # Define other URLs here
]
