# from django.shortcuts import render

# # Create your views here.

from django.views import generic

class SkinView(generic.TemplateView):
    template_name = "SkinDiseaseInformation.html"

# class IndexView(generic.TemplateView):
#     template_name = "AtopicSkin.html"