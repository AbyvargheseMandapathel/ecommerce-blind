from django.urls import path
from ecommerce import views
from ecommerce.views import login_view
from .views import product_details


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('product/<int:product_id>/', product_details, name='product_details'),
    # Define other URLs here
]
