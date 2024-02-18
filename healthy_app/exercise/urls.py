from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('get_exercises/', views.ExerciseAPIView.as_view(), name='exercise'),
]
