"""
URL configuration for mainproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("about", views.about, name="about"),
    path("web", views.web, name="web"),
    path("home1", views.home1, name="home1"),
    path("home2", views.home2, name="home2"),
    path("home3", views.home3, name="home3"),
    path("add", views.add, name="add"),
    path("add1", views.add1, name="add1"),
    path("addata", views.addata, name="addata"),
    path("admissionform", views.admissionform, name="admissionform"),
    path("feedback", views.feedback, name="feedback"),
    path('register/' , views.register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('home01', views.home01, name='home01'),
]

