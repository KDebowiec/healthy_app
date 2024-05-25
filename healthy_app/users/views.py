from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views import View, generic
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import HealthyAppUser


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

# class RegisterView(CreateView):
#     model = User
#     fields = ['username', 'email', 'password']
#     register_form = UserRegisterForm
#     success_url = reverse_lazy('base')
#     template_name = 'users/register.html'


# class RegisterView(View):
#     def get(self, request, *args, **kwargs):
#         form = UserRegisterForm()
#         return render(request, 'users/register.html', {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('base')
#         return render(request, 'nutrition/nutrition.html', {'form': form})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Przekierowanie do strony po zalogowaniu
        else:
            return HttpResponse('Nieprawidłowe dane logowania')


# class RegisterView(View):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.succes(request, 'konto zostało utworzone!')
#             return redirect('base')
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'register.html', {'form': form})

