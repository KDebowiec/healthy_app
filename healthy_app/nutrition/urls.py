from . import views
from django.contrib import admin
from django.urls import path
from . import views as main_views

urlpatterns = [
    # path('get_nutrition/', views.NutritionView.as_view(), name='get_nutrition'),
    path('get_nutrition/', views.NutritionView.as_view(), name='get_nutrition'),
    path('', main_views.MainView.as_view(), name='base'),
    # path('show_nutrition/', views.ConvertingNutrition.as_view(), name='nutrition'),
]
