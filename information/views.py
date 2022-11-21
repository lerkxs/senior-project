# from django.shortcuts import render

# # Create your views here.

from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "Skin disease information.html"

class IndexView(generic.TemplateView):
    template_name = "AtopicSkin.html"