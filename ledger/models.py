from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", args=[self.pk])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe")
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name="ingredients")

    def __str__(self):
        return f"{self.quantity} of {self.ingredient} for {self.recipe}"