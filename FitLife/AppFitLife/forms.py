from django import forms


class HeroesForm(forms.Form):
    name=forms.CharField(max_length=50)
    surname=forms.CharField(max_length=50)
    achievements=forms.CharField(max_length=50)


class ExercisesForm(forms.Form):
    name=forms.CharField(max_length=50)
    description=forms.CharField(max_length=50)
    
    
class FoodsForm(forms.Form):
    name= forms.CharField(max_length=50)
    recipe= forms.CharField(max_length=50)
    calories=forms.IntegerField()