"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from company_role.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', company_Register,name='company_Register'),
    path('dashboard_index', dashboard_index,name='dashboard_index'),
    path('', Admin_login,name='Admin_login'),
    path('add_language', create_language,name='create_language'),
    path('get_language', get_language,name='get_language'),
    path('add_level', create_level,name='create_level'),
    path('get_level', get_level,name='get_level'),
    path('get_allcompanies', get_allcompanies,name='create_level'),
    path('add_questions', add_questions,name='add_questions'),
    path('create_sample_paper', create_sample_paper,name='create_sample_paper')
]
