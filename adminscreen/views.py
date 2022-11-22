from django.shortcuts import render
from django.views import generic

class AdminView(generic.TemplateView):
    template_name = "Admin_SkinDiseaseInformation.html"   
