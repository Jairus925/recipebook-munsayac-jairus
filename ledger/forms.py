from django.forms import ModelForm
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "author"]

class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ["ingredient", "quantity"]

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]

class RecipeImageForm(ModelForm):
    class Meta:
        model = RecipeImage
        fields = ["image", "description"]