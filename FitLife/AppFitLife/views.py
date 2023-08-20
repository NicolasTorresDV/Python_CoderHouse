from django.http import HttpResponse
from .models import Heroes , Food , Exercises
from django.shortcuts import render
from .forms import ExercisesForm, HeroesForm, FoodsForm


# Renders

def exercises(request):
    return render(request,"AppFitLife/exercises.html")

def foods(request):
    return render(request,"AppFitLife/foods.html")

def heroes(request):
    return render(request,"AppFitLife/heroes.html")

def index(request):
    return render(request,"AppFitLife/index.html")

def searchFood(request):
    return render(request, "AppFitLife/searchFood.html")


# Renders End


def exercises(request):
    exercises= Exercises.objects.all()
    if request.method=="POST":
        form=ExercisesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            name=info["name"]
            description=info["description"]
            exercise=Exercises(name=name,description=description)
            exercise.save()
            form_exercises=ExercisesForm()
            return render(request,"AppFitLife/exercises.html", {"mensaje":"Exercise created", "formulario":form_exercises })
        else:
            return render(request,"AppFitLife/exercises.html", {"mensaje":"Invalid data"})
    else:
        form_exercises=ExercisesForm()

    return render(request,"AppFitLife/exercises.html", {"form":form_exercises , "exercises": exercises})


def foods(request):
    foods= Food.objects.all()
    if request.method=="POST":
        form=FoodsForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            name=info["name"]
            recipe=info["recipe"]
            calories=info["calories"]
            food=Food(name=name,recipe=recipe,calories=calories)
            food.save()
            form_foods=FoodsForm()
            return render(request,"AppFitLife/foods.html", {"mensaje":"Food created", "formulario":form_foods})
        else:
            return render(request,"AppFitLife/foods.html", {"mensaje":"Invalid data"})
    else:
        form_foods=FoodsForm()

    return render(request,"AppFitLife/foods.html", {"form":form_foods , "foods": foods})

def heroes(request):
    heroes= Heroes.objects.all()
    if request.method=="POST":
        form=HeroesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            name=info["name"]
            surname=info["surname"]
            achievements=info["achievements"]
            hero=Heroes(name=name,surname=surname,achievements=achievements)
            hero.save()
            form_heroes=HeroesForm()
            return render(request,"AppFitLife/heroes.html", {"mensaje":"Hero created", "formulario":form_heroes})
        else:
            return render(request,"AppFitLife/heroes.html", {"mensaje":"Invalid data"})
    else:
        form_heroes=HeroesForm()

    return render(request,"AppFitLife/heroes.html", {"form":form_heroes , "heroes": heroes})

def search(request):
    foodName=request.GET["name"]
    if foodName!="":
        foods=Food.objects.filter(name__icontains=foodName)
        return render(request,"AppFitLife/searchResults.html", {"foods":foods})
    else:
        return render(request,"AppFitLife/searchFood.html", {"mensaje":"Food name is empty!"})