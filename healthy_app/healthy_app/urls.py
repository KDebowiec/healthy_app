from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exercises/', include('exercise.urls')),
    path('nutrition/', include('nutrition.urls')),
]
