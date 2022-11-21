from django.urls import path, include
from django.contrib.auth import views as auth_views
from signup import views
 
 
urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("home/", views.home, name='home'),
]