import urllib
from django.shortcuts import render
import requests
import json
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import NutritionGeneralForm
from exercise.forms import ExerciseForm
from users.forms import UserRegisterForm
from bs4 import BeautifulSoup
from .models import MealPlan
from django.core.mail import send_mail
from healthy_app.settings import EMAIL_HOST_USER

class MainView(TemplateView):
    template_name = 'nutrition/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercise_form'] = ExerciseForm()
        context['nutrition_form'] = NutritionGeneralForm()
        context['register_form'] = UserRegisterForm()
        return context


class NutritionView(TemplateView):
    template_name = 'nutrition/show_nutrition.html'


    def get(self, request):
        form = NutritionGeneralForm(request.GET)
        return render(request, 'nutrition/nutrition.html', {'form': form})

    def post(self, request):
        form = NutritionGeneralForm(request.POST)
        if form.is_valid():
            size = 1
            general_health = form.cleaned_data['general_health']
            general_min_kcal = form.cleaned_data['general_min_kcal']
            general_max_kcal = form.cleaned_data['general_max_kcal']
            email = form.cleaned_data['email']
            print(general_max_kcal)
            diet_plan_request = {"size": size, "plan": {"accept": {"all": [{"health": general_health}]}, "fit": {"ENERC_KCAL": {"min": general_min_kcal, "max": general_max_kcal}}, "sections": {"Breakfast": {"accept": {"all": [{"meal": ["breakfast"]}]}}, "Lunch": {"accept": {"all": [{"meal": ["lunch/dinner"]}]}}, "Dinner": {"accept": {"all": [{"meal": ["lunch/dinner"]}]}}}}}
            nutrition_api_key = settings.NUTRITION_API_KEY
            nutrition_id = settings.NUTRITION_ID
            api_url = f'https://api.edamam.com/api/meal-planner/v1/{nutrition_id}/select'
            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Basic YTdkZWI3MDg6MmY4N2IxOTc4YTExMmU2YThhYjc1M2Y3YjI4ZmU2YWM=',
                'Edamam-Account-User': '1',
            }
            response = requests.post(api_url, data=json.dumps(diet_plan_request), headers=headers)
            response = response.json()
            data = response
            list_of_links = []
            for i in range(size):
                list_of_links.append(data['selection'][i]['sections']['Breakfast']['assigned'])
                list_of_links.append(data['selection'][i]['sections']['Dinner']['assigned'])
                list_of_links.append(data['selection'][i]['sections']['Lunch']['assigned'])

            headers2 = {
                'accept': 'application/json',
                'Accept-Language': 'en',
                'Edamam-Account-User': '1',
            }
            recipes = []
            for link in list_of_links:
                nutrition_api_key = '2f87b1978a112e6a8ab753f7b28fe6ac'
                nutrition_id = 'a7deb708'
                api_endpoint = 'https://api.edamam.com/api/recipes/v2/by-uri?type=public&'
                request_body = urllib.parse.quote_plus(f'uri={link}&app_id={nutrition_id}&app_key={nutrition_api_key}&field=url&field=image&field=ingredients&field=totalNutrients', safe='=&')
                api_url = f'{api_endpoint}{request_body}'
                recipe = requests.get(api_url, headers=headers2)
                recipes.append(recipe.json())

            sorted_data = []

            for element in recipes:
                list_of_ingredients = []
                for value in element['hits'][0]['recipe']['ingredients']:
                    list_of_ingredients.append(value['text'])

                def get_page_title(url):
                    try:
                        response = requests.get(url)
                        response.raise_for_status()
                        soup = BeautifulSoup(response.text, 'html.parser')
                        page_title = soup.title.string

                        return page_title
                    except Exception as e:

                        return 'tytul'

                page_title = get_page_title(element['hits'][0]['recipe']['url'])

                sorted_data.append(
                        {'image': element['hits'][0]['recipe']['image'], 'url': element['hits'][0]['recipe']['url'],
                         'ingredients': list_of_ingredients, 'page_title': page_title})
                photo = element['hits'][0]['recipe']['image']

            print(sorted_data)

            send_mail(
                "Welcome to Healthy_App",
                "You just got your diet meal plan on healthy_app, congrats!",
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            MealPlan.objects.create(user=self.request.user, meal_json=recipes, general_health=general_health, general_min_kcal=general_min_kcal, general_max_kcal=general_max_kcal, photo=photo, page_title=page_title)

            # send_mail

            return render(request, self.template_name, {'sorted_data': sorted_data})

        else:
            print('Formularz nie działa')
            return HttpResponse('Błąd formularza')


