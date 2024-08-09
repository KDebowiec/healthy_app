from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views import View, generic
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from nutrition.models import MealPlan
from exercise.models import Exercises
from bs4 import BeautifulSoup
import requests


class AjaxRegisterView(View):

    # def get_context_data(self, **kwargs):
    #     context['register_form'] = UserRegisterForm()
    #     return context

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')  # Przekierowanie do strony po zalogowaniu
        else:
            return HttpResponse('Nieprawidłowe dane logowania')


class ProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile.html'
    succes_url = reverse_lazy('users:profile')

    def get(self, request, *args, **kwargs):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated")
            return redirect(self.success_url)

        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})


class ShowPlans(View):
    def get(self, request, *args, **kwargs):
        mealplans = MealPlan.objects.filter(user=request.user)
        recipes = []

        for element in mealplans:
            recipes.append(element.meal_json[0])

        print(recipes )

        sorted_data = []

        for e in recipes:
            list_of_ingredients = []
            for value in e['hits'][0]['recipe']['ingredients']:
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

            page_title = get_page_title(e['hits'][0]['recipe']['url'])

            sorted_data.append(
                {'image': e['hits'][0]['recipe']['image'], 'url': e['hits'][0]['recipe']['url'],
                 'ingredients': list_of_ingredients, 'page_title': page_title})
            photo = e['hits'][0]['recipe']['image']

        print(sorted_data)

        return render(request, 'users/show_plans.html', {'sorted_data': sorted_data})


class ShowExercises(ListView):
    model = Exercises
    template_name = 'users/show_workouts.html'
    def get_queryset(self):
        return Exercises.objects.filter(user=self.request.user)