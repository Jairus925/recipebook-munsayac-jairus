from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length=200)

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