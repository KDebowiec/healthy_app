from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import ProfileView, ShowPlans, ShowExercises
from . import ajax_datatable_views
app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('ajax/register/', views.AjaxRegisterView.as_view(), name='ajax_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('show-plans/', ShowPlans.as_view(), name='show-plans'),
    path('show-exercises/', ShowExercises.as_view(), name='show-exercises'),
    path('ajax/datatable/nutrition/', ajax_datatable_views.NutritionAjaxDatatableView.as_view(), name="ajax_datatable_nutrition"),
    path('ajax/datatable/workouts/', ajax_datatable_views.WorkoutsAjaxDatatableView.as_view(), name="ajax_datatable_workouts"),
]