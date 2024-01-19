from django.shortcuts import render, redirect #import things
from .models import * #import models
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q,Sum
from .field import decompress_data
from django.core.paginator import Paginator
# Create your views here.

@login_required(login_url="/login/")
def recipe(request): 
   queryset = Recipe.objects.all()
   for recipe in queryset:
       if recipe.image_data:
           recipe.image_data = decompress_data(recipe.image_data)
   if request.GET.get("search"):
       queryset = queryset.filter(recipe_name__icontains=request.GET.get("search"))
   paginator=Paginator(queryset,4)
   page_no=request.GET.get('page')
   queryset=paginator.get_page(page_no)
   context = {'recipes': queryset}
   return render(request, 'recipe.html', context)




def about(request):
    return render(request,'about.html')


from PIL import Image
import io

def add_recipe(request):
   if request.method == "POST":
       data = request.POST
       recipe_name = data.get('recipe_name')
       recipe_description = data.get('recipe_description')
       image_data = request.FILES.get('recipe_image')
       user = request.user
       if image_data:
           if image_data.size > 1268576: # 1 MB = 1048576 bytes
               messages.error(request, 'Image size should not exceed 1MB')
               return redirect('/add_recipe/')
           else:
               img = Image.open(image_data)
               output = io.BytesIO()
               img.save(output, format='JPEG', quality=20) # Always save as JPEG
               image_data = output.getvalue()
       Recipe.objects.create(
           user=user,
           recipe_name=recipe_name,
           recipe_description=recipe_description,
           image_data=image_data
       )
       return redirect('/recipe/')
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


