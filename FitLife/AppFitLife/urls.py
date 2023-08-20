from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("index", index, name="index"),
    path('exercises/', exercises, name="exercises"),
    path('foods/', foods, name="foods"),
    path('heroes/', heroes, name="heroes"),
    path('searchFood/', searchFood, name="searchFood"),
    path('searchResults/', search, name="search"),
]
