from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('colleges/', views.colleges),
    path('students/', views.students),
    path('address/', views.address),
    path('contact_us/', views.contact_us),
    path('login/', views.login, name='login'),
    path('loginverification/', views.loginverification, name='loginverification'),    
]
