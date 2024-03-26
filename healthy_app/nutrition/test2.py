# class NutritionView(TemplateView):
#     template_name = 'nutrition/show_nutrition.html'
#
#     def get(self, request):
#         form = NutritionGeneralForm(request.GET)
#         return render(request, 'nutrition/nutrition.html', {'form': form})
#
#     def post(self, request):
#         form = NutritionGeneralForm(request.POST)
#         if form.is_valid():
#             size = form.cleaned_data['size']
#             general_health = form.cleaned_data['general_health']
#             general_min_kcal = form.cleaned_data['general_min_kcal']
#             general_max_kcal = form.cleaned_data['general_max_kcal']
#             diet_plan_request = {"size": size, "plan": {"accept": {"all": [{"health": general_health}]}, "fit": {"ENERC_KCAL": {"min": general_min_kcal, "max": general_max_kcal}}, "sections": {"Breakfast": {"accept": {"all": [{"meal": ["breakfast"]}]}}, "Lunch": {"accept": {"all": [{"meal": ["lunch/dinner"]}]}}, "Dinner": {"accept": {"all": [{"meal": ["lunch/dinner"]}]}}}}}
#             nutrition_api_key = settings.NUTRITION_API_KEY
#             nutrition_id = settings.NUTRITION_ID
#             api_url = f'https://api.edamam.com/api/meal-planner/v1/{nutrition_id}/select'
#             headers = {
#                 'Content-type': 'application/json',
#                 'Accept': 'application/json',
#                 'Authorization': 'Basic YTdkZWI3MDg6MmY4N2IxOTc4YTExMmU2YThhYjc1M2Y3YjI4ZmU2YWM=',
#                 'Edamam-Account-User': '1',
#             }
#             response = requests.post(api_url, data=json.dumps(diet_plan_request), headers=headers)
#             response = response.json()
#             data = response
#             list_of_links = []
#             for i in range(size):
#                 list_of_links.append(data['selection'][i]['sections']['Breakfast']['assigned'])
#                 list_of_links.append(data['selection'][i]['sections']['Dinner']['assigned'])
#                 list_of_links.append(data['selection'][i]['sections']['Lunch']['assigned'])
#
#             print(list_of_links)
#             headers2 = {
#                 'accept': 'application/json',
#                 'Accept-Language': 'en',
#                 'Edamam-Account-User': '1',
#             }
#             recipes = []
#             for link in list_of_links:
#                 nutrition_api_key = '2f87b1978a112e6a8ab753f7b28fe6ac'
#                 nutrition_id = 'a7deb708'
#                 api_endpoint = 'https://api.edamam.com/api/recipes/v2/by-uri?type=public&'
#                 request_body = urllib.parse.quote_plus(f'uri={link}&app_id={nutrition_id}&app_key={nutrition_api_key}&field=url&field=image&field=ingredients&field=totalNutrients', safe='=&')
#                 api_url = f'{api_endpoint}{request_body}'
#                 recipe = requests.get(api_url, headers=headers2)
#                 recipes.append(recipe.json())
#
#
#         else:
#             print('Formularz nie działa')
#             return HttpResponse('Błąd formularza')
#
# class Recipe:
#     name = 'test'
#     frog = 3
#
# recipe = Recipe
# recipes.append(recipe)
# return render(request, self.template_name, {'recipes': recipes})


