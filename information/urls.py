from django.urls import path

from . import views


app_name = 'information'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('AtopicSkin/',views.IndexView.as_view(), name="AtopicSkin"),
]