from django.urls import path
from ecommerce import views
from ecommerce.views import login_view


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup_success/', views.signup_success, name='signloginsignup_success'),
    path('login/', login_view, name='login'),
    path('login_success/', views.login_success, name='login_success'),
    
    # Define other URLs here
]
