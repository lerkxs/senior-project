from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('top.urls')),
    path('signup/', include('signup.urls')),
    path('information/', include('information.urls')),
    path('adminscreen/', include('adminscreen.urls')),
    path('blog/', include('blog.urls')),
]
