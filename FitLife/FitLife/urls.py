from django.contrib import admin
from django.urls import path, include
from AppFitLife.views import heroes , foods, exercises,index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("index", index, name="index"),
    path("AppFitLife/", include("AppFitLife.urls")),
]
