from django.urls import path

from . import views

app_name='administrator'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    # path('', views.IndexView.as_view(), name="administrator"),
    path('Admini_SkinDiseaseInformation/', views.IndexView.as_view(), name="Admin_SkinDiseaseInformation"),
]
