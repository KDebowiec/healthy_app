from rest_framework import views
from django.shortcuts import render
import requests
import json
# from ..healthy_app.settings import EXERCISE_API_KEY
from .forms import NutritionGeneralForm
from django.http import JsonResponse
# api key =  f63a7889f0c15a63f57afff8a54cfadf
# api id = 6ae86d85
# request url = https://api.edamam.com/api/nutrition-details?app_id=f63a7889f0c15a63f57afff8a54cfadf&app_key=6ae86d85
from py_edamam import Edamam
from django.conf import settings
from django.http import HttpResponse


# DPR = {
#   "size": 7,
#   "plan": {
#     "accept": {
#       "all": [
#         {
#           "health": [
#             "SOY_FREE",
#             "FISH_FREE",
#             "MEDITERRANEAN"
#           ]
#         }
#       ]
#     },
#     "fit": {
#       "ENERC_KCAL": {
#         "min": 1000,
#         "max": 2000
#       },
#     },
#     "sections": {
#       "Breakfast": {
#         "accept": {
#           "all": [
#             {
#               "dish": []
#             },
#             {
#               "meal": [
#                 "breakfast"
#               ]
#             }
#           ]
#         },
#         "fit": {
#           "ENERC_KCAL": {}
#         }
#       },
#       "Lunch": {
#         "accept": {
#           "all": [
#             {
#               "dish": []
#             },
#             {
#               "meal": [
#                 "lunch/dinner"
#               ]
#             }
#           ]
#         },
#         "fit": {
#           "ENERC_KCAL": {}
#         }
#       },
#       "Dinner": {
#         "accept": {
#           "all": [
#             {
#               "dish": []
#             },
#             {
#               "meal": [
#                 "lunch/dinner"
#               ]
#             }
#           ]
#         },
#         "fit": {
#           "ENERC_KCAL": {}
#         }
#       }
#     }
#   }
# }


class NutritionAPIView(views.APIView):

    def get(self, request):
        if request.method == 'GET':
            form = NutritionGeneralForm(request.GET)
            return render(request, 'nutrition/nutrition.html', {'form': form})

    def post(self, request):
        form = NutritionGeneralForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data['size']
            general_health = form.cleaned_data['general_health']
            general_min_kcal = form.cleaned_data['general_min_kcal']
            general_max_kcal = form.cleaned_data['general_max_kcal']
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
            request.session['data'] = response
            request.session['size'] = size
            return render(request, 'nutrition/show_nutrition.html', {'data': response, 'size': size})
        else:
          print('Formularz nie działa')
          return HttpResponse('Błąd formularza')


class ConvertingNutrition(views.View):

    def data_from_api(self, request):
        data = request.session.get('data')
        size = request.session.get('size')

        list_of_links = []
        for i in range(size):
            list_of_links.append(data['selection'][i]['sections']['Breakfast']['assigned'])
            list_of_links.append(data['selection'][i]['sections']['Dinner']['assigned'])
            list_of_links.append(data['selection'][i]['sections']['Lunch']['assigned'])

        request.session['list'] = list_of_links

    def get(self, request):
        data = request.session.get('list')
        nutrition_api_key = settings.NUTRITION_API_KEY
        nutrition_id = settings.NUTRITION_ID
        api_endpoint = 'https://api.edamam.com/api/meal-planner/v1/'

        for element in data:
            api_url = f'{api_endpoint}/{element}?type=public&app_id={nutrition_id}&app_key={nutrition_api_key}'
            response = requests.get(api_url)
            print(response)
