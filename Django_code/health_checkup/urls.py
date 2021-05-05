from django.urls import path
from health_checkup import views

urlpatterns = [
    path('', views.health_checkup, name='health_checkup'),
    path('data/', views.patient_data),
    path('view/', views.view,name='view'),
    path('logout', views.logout,name='logout'),
]