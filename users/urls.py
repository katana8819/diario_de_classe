from django.urls import path
from django.contrib.auth import views as auth_views
 
 app_name='users'
 
 urlpatterns=[
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
 ]
