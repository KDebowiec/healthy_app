from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('get_nutrition/', views.NutritionAPIView.as_view(), name='get_nutrition'),
    path('nutrition/', views.NutritionAPIView.as_view(), name='nutrition'),
    path('show_nutrition/', views.NutritionAPIView.as_view(), name='nutrition'),
]
