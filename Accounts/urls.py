from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('login/', my_login, name='login'),
    path('edit/', edit_user, name='edit_user'),
    path('data/', user_data, name='user_data'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]