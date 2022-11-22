from django.urls import path, include
from django.contrib.auth import views as auth_views
from signup import views
 
app_name = 'signup' 

urlpatterns = [
    path('', views.LoginView.login, name='login'),
    # path('', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("home/", views.HomeView.home, name='home'),
    # path("home/", views.home, name='home'),
]