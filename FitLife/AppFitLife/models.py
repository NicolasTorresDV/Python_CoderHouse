from django.db import models


class Exercises(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} - {self.description}"

class Food(models.Model):
    name=models.CharField(max_length=50)
    recipe=models.CharField(max_length=50)
    calories=models.IntegerField()
    def __str__(self):
        return f"{self.name} - {self.recipe} - {self.calories}"
    

class Heroes(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    achievements=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} {self.surname} - {self.achievements}"
