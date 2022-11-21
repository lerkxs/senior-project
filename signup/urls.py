from django.urls import path, include
from django.contrib.auth import views as auth_views
from signup import views
 
app_name = 'signup' 

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("home/", views.HomeView.as_view(), name='home'),
]