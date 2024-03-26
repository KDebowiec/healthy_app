from . import views
from django.contrib import admin
from django.urls import path
from . import views as main_views

urlpatterns = [
    # path('get_nutrition/', views.NutritionView.as_view(), name='get_nutrition'),
    path('nutrition/', views.NutritionView.as_view(), name='nutrition'),
    path('', main_views.mainView.as_view(), name='base'),
    # path('show_nutrition/', views.ConvertingNutrition.as_view(), name='nutrition'),
]
