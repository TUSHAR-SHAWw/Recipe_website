"""
URL configuration for Recipe_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Recipe_App.views import *
from django.conf import settings#just copy paste all imports
from django.conf.urls.static import static
from django.contrib import admin
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('about/',about, name="about"),
    path('',recipe, name="recipe"),
    path('recipe/',recipe, name="recipe"),
    path('add_recipe/',add_recipe, name="add_recipe"),
    path('login/',login_page, name="login_page"),
    path('logout/',logout_page, name="logout_page"),
    path('register/',register, name="register"),
    path('delete_recipe/<id>/',delete_recipe, name="delete_recipe"),
    path('update_recipe/<id>/',update_recipe, name="update_recipe"),
    path('admin/', admin.site.urls),
]