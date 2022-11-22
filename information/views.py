from django.views import generic
# 未ログインユーザーをログインページにリダイレクトさせる(第一引数に指定)
from django.contrib.auth.mixins import LoginRequiredMixin

class SkinView(generic.TemplateView):
    template_name = "SkinDiseaseInformation.html"

class AtopicView(generic.TemplateView):
    template_name = "AtopicSkin.html"