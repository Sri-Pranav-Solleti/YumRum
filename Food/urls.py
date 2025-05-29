"""
URL configuration for Food project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Foodproject.views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register, name='register'),
    path('login/', login_view, name='login_view'),
    path('', login_required(home1, login_url='login_view'), name='home1'),
    path('aboutus/', login_required(aboutus, login_url='login_view'), name='aboutus'),
    path('reservation/', login_required(reservation, login_url='login_view'), name='reservation'),
    path('menu/', login_required(menu, login_url='login_view'), name='menu'),
    path('confirm/', login_required(confirm, login_url='login_view'), name='confirm'),
    path('register/', register, name='register'),
    path('end/', login_required(end, login_url='login_view'), name='end'),
    path('reserverty/', login_required(thank, login_url='login_view'), name='thank'),
    path('reviews/',login_required(reviews,login_url='login_view'),name='reviews'),
    path('logout/', logout_view, name='logout'),
    path('placeorder/', login_required(placeorder, login_url='login_view'), name='placeorder'),
    path('feedback/',login_required(feedback,login_url='login_view'),name='feedback'),
    path('gallery/',login_required(gallery,login_url='login_view'),name='gallery'),
    path('contactus/',login_required(contactus,login_url='login_view'),name='contactus'),
    
]
if settings.DEBUG:  # Serve media files only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
