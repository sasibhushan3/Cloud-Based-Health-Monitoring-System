from django.urls import path
from accounts import views

urlpatterns = [
    # path('', views.register, name='register'),
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('login/login', views.login),
    path('login/register', views.register),
    path('register/userdata/', views.userdata),
]