"""week2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from myproject import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('creates/',views.CreatePersonView.as_view(), name='person'),
    path('login/',auth_views.login,{'template_name': 'myproject/templates/registration/login.html'}, name='login'),
    path('home/',TemplateView.as_view(template_name='home.html'), name='home'),
    path('logout/',auth_views.logout,{'template_name': 'myproject/templates/registration/logout.html'}, name='logout'),
    path('profiles/',TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('rent/',views.CreateRentView.as_view(), name='rent'),
    # path('add-rent/',views.addRent, name='addRent'),
    ##path('car/',TemplateView.as_view(template_name='car.html'), name='car'),
    path('car/',views.getAllCar, name='car'),
    # path('accounts/profile/',views.CreateProfileView.as_view(), name='profile'),


]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
