from django.urls import path
from ecommerce import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # Define other URLs here
]
