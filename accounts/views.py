from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm,CustomAuthenticationForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from restaurant_app.models import Rest_detail

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rest_detail'] = Rest_detail.objects.first()  # Get the first object
        return context



class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('restaurant_app:home')
    # redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rest_detail'] = Rest_detail.objects.first()  # Get the first object
        return context




def check_auth(request):
    return JsonResponse({'authenticated': request.user.is_authenticated})
