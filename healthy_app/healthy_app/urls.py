from django.contrib import admin
from django.urls import path, include
from ..users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exercises/', include('exercise.urls')),
    path('nutrition/', include('nutrition.urls')),
    path('register/', user_views.register, name='register'),
]
