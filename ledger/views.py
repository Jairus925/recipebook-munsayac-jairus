from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeForm, RecipeIngredientForm, IngredientForm, RecipeImageForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})

@login_required
def recipe_detail_database(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    return render(request, 'recipe_detail.html',{'name': recipe.name, "ingredients":ingredients, "author": recipe.author, 'recipe': recipe})

@login_required
def recipeingredient_add(request, recipe_id):
    if request.method == "POST":
        recipeingredient_form = RecipeIngredientForm(request.POST)
        if recipeingredient_form.is_valid():
            recipe = Recipe.objects.get(pk=recipe_id)
            recipeingredient = recipeingredient_form.save(commit=False)
            recipeingredient.recipe = recipe
            recipeingredient.save()
        return HttpResponseRedirect(reverse("detail", args=[recipe_id]))

    return render(
        request,
        "recipeingredient_add.html",
        {"recipeingredient_form": RecipeIngredientForm(), "recipe_id": recipe_id},
    )


@login_required
def recipeimage_add(request, recipe_id):
    if request.method == "POST":
        recipeimage = RecipeImage(recipe=Recipe.objects.get(pk=recipe_id))
        print(request.FILES)
        recipeimage_form = RecipeImageForm(
            request.POST, request.FILES, instance=recipeimage
        )
        if recipeimage_form.is_valid():
            recipeimage_form.save()

        return HttpResponseRedirect(reverse("detail", args=[recipe_id]))
    return render(
        request,
        "recipeimage_add.html",
        {"recipeimage_form": RecipeImageForm(), "recipe_id": recipe_id},
    )


@login_required
def ingredient_add(request):
    if request.method == "POST":
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid():
            ingredient_form.save()
        return HttpResponseRedirect(reverse("recipe_list"))

    return render(
        request,
        "ingredient_add.html",
        {"ingredient_form": IngredientForm()},
    )


@login_required
def recipe_add(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save()
            if "add_ingredient" in request.POST:
                return redirect(reverse("ingredient_add"))
            return HttpResponseRedirect(reverse("recipe_list"))

    return render(request, "recipe_add.html", {"recipe_form": RecipeForm()})

