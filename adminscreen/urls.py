from django.urls import path

from . import views

app_name='administrator'
urlpatterns = [
    path('', views.AdminView.as_view(), name="Admin_SkinDiseaseInformation"),
]
