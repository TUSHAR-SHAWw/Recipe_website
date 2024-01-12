from django.shortcuts import render, redirect #import things
from .models import * #import models
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q,Sum

# Create your views here.

@login_required(login_url="/login/")
def recipe(request):  
    quertset= Recipe.objects.all()
    if request.GET.get("search"):
        quertset=quertset.filter(recipe_name__icontains=request.GET.get("search"))
    context={'recipes':quertset}
    return render(request, 'recipe.html', context)

def about(request):
    return render(request,'about.html')
def add_recipe(request):
    if request.method =="POST":#this runs after hitting submit button
            data = request.POST
            recipe_name = data.get('recipe_name')
            recipe_description = data.get('recipe_description')
            image_data = request.FILES.get('recipe_image')
            user = request.user # Get the current logged-in user
            if image_data:
                image_data=image_data.read()
            Recipe.objects.create(
            user=user, # Provide the user when creating a new Recipe
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            image_data=image_data#binary field
        )
            return redirect('/recipe/')#after submiting redirect the so it doesnt contain previous data
    return render(request,'add_recipe.html')


def delete_recipe(request,id):
    quaryset= Recipe.objects.get(id=id)
    quaryset.delete()
    return redirect("/recipe/")#refreash page after delete
def update_recipe(request,id):
    queryset= Recipe.objects.get(id=id)
    if request.method =="POST":#this runs after hitting submit button
        data=request.POST
        recipe_name=data.get("recipe_name")
        recipe_description=data.get("recipe_description")
        image_data=request.FILES.get('recipe_image')
        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description
        if image_data:
            queryset.image_data=image_data.read()
        queryset.save()
        return redirect("/recipe/")#refreash page after update
    context={"recipe":queryset}
    return render(request,"update_recipe.html",context)

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        username= request.POST.get("username")
        
        # Check if the email is already registered
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "This email is already registered.")
            return redirect("/register/")
        
        # Create a new user if the email is not already registered
        new_user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        messages.success(request, "You're registered.")
        return redirect("/register/")  # Redirect to registration page after successful registration
    
    return render(request, "register.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
           messages.info(request, "Incorrect Username")
           return redirect("/login/")
        user= authenticate(request, username=username,password=password)
        if user is None:
            print(f"Login failed for username: {username} with password: {password} ,{user}")
            messages.info(request, "Incorrect Password")
            return redirect("/login/")
        else:
            login(request,user)
            context={"user":user}
            return redirect("/recipe/",context)
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect("/login/")


