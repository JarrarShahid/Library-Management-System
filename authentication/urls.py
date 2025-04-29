from django.urls import path
from .views import custom_login,logout_view

urlpatterns = [
    path('login/', custom_login, name='custom_login'),
    path('logout/', logout_view, name='logout'),
]