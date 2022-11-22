from django.urls import path

from . import views


app_name = 'information'
urlpatterns = [
    path('', views.SkinView.as_view(), name="SkinDiseaseInformation"),
    path('AtopicSkin/',views.AtopicView.as_view(), name="AtopicSkin"),
]