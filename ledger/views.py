from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, RecipeIngredient

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})




    
def recipe_detail_database(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    return render(request, 'recipe_detail.html',{'name': recipe.name, "ingredients":ingredients})