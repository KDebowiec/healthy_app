from rest_framework import views
from django.shortcuts import render
import requests
from .settings import EXERCISE_API_KEY
from .forms import ExerciseForm


# class ExerciseFormView(views.View):
#     def get(self, request):
#         return render(request, 'exercise_template.html')
#
#     def post(self, request):
#         muscle = request.POST.get('muscle')
#
#         api_view = ExerciseAPIView()
#         response = api_view.get(request, muscle=muscle)


class ExerciseAPIView(views.APIView):
    def get_exercise(self, request, muscle=None):
        if request.method == 'GET':
            form = ExerciseForm(request.GET)
            return render(request, 'healthy_app/exercise.html', {'form': form})
        elif request.method == 'POST':
            muscle = request.form['muscle']
            api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
            exercise_api_key = EXERCISE_API_KEY
            response = requests.get(api_url, headers={'X-Api-Key': {exercise_api_key}})
            print(response)