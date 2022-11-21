from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

 
class LoginView(LoginRequiredMixin,generic.TemplateView):
    template_name = "login.html"

# def login(request):
#     return render(request, 'login.html')


class HomeView(generic.TemplateView, LoginRequiredMixin):
    template_name = "home.html"

# @login_required
# def home(request):
#     return render(request, 'home.html')
