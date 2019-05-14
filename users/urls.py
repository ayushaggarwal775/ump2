from django.urls import path
from . import views

urlpatterns = [path('', views.Home.index), path('add-user/', views.AddUser.add_user),
               path('login/', views.Auth.user_login), path('logout/', views.Auth.logout)]
