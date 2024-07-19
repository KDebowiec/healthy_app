from rest_framework import views
from rest_framework.response import Response
from django.shortcuts import render
from django.conf import settings
import requests
from .forms import ExerciseForm
from django.http import JsonResponse
from .models import Exercises
from django.views.generic import TemplateView


class ExerciseView(TemplateView):
    template_name = 'exercise/show_exercises.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.request.session.get('data')
        return context

    def get(self, request):
        form = ExerciseForm(request.GET)
        return render(request, 'exercise/exercise.html', {'form': form})

    def post(self, request):
        form = ExerciseForm()
        difficulty = request.POST['difficulty']
        muscle = request.POST['muscle']
        exercise_api_key = settings.EXERCISE_API_KEY
        api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={muscle}&difficulty={difficulty}'
        response = requests.get(api_url, headers={'X-Api-Key': exercise_api_key})
        api_data = response.json()
        new_exercise = Exercises(user=self.request.user, descriptions=api_data, muscle=muscle, difficulty=difficulty)
        new_exercise.save()
        # muscle = form.cleaned_data['muscle']
        # difficulty = form.cleaned_data['difficulty']
        return render(request, 'exercise/show_exercises.html', {'api_data': api_data})

