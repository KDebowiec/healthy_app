from rest_framework import views
from rest_framework.response import Response
from django.shortcuts import render
from django.conf import settings
import requests
from .forms import ExerciseForm
from django.http import JsonResponse
from .models import Exercises


class ExerciseAPIView(views.APIView):

    def get(self, request):
        if request.method == 'GET':
            form = ExerciseForm(request.GET)
            return render(request, 'exercise/exercise.html', {'form': form})

    def post(self, request):
        email = request.POST['email']
        muscle = request.POST['muscle']
        difficulty = request.POST['difficulty']
        exercise_api_key = settings.EXERCISE_API_KEY
        api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={muscle}&difficulty={difficulty}'
        response = requests.get(api_url, headers={'X-Api-Key': exercise_api_key})
        api_data = response.json()
        new_exercise = Exercises(email=email, descriptions=api_data)
        new_exercise.save()
        return render(request, 'exercise/show_exercises.html', {'api_data': api_data})

