from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
# 未ログインユーザーをログインページにリダイレクトさせる(第一引数に指定)
from django.contrib.auth.mixins import LoginRequiredMixin

 
class LoginView(LoginRequiredMixin):
    # template_name = "login.html"
    def login(request):
        return render(request, 'signup/login.html')


class HomeView(LoginRequiredMixin):
    # template_name = "home.html"

    @login_required
    def home(request):
        return render(request, 'signup/home.html')
