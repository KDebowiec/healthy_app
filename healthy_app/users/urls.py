from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('ajax/register/', views.AjaxRegisterView.as_view(), name='ajax_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]