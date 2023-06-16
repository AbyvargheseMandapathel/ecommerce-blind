from django.urls import path
from ecommerce import views
from ecommerce.views import login_view

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    # Define other URLs here
]
