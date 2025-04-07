from django.urls import path
from .views import recipe_list, recipe_detail_database, recipe_add,recipeingredient_add, ingredient_add, recipeimage_add
urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', recipe_detail_database, name='detail'),
    path(
        "recipe/<int:recipe_id>/add_ingredient",
        recipeingredient_add,
        name="recipeingredient_add",
    ),
    path(
        "recipe/<int:recipe_id>/add_image",
        recipeimage_add,
        name="recipeimage_add",
    ),
    path("add_ingredient", ingredient_add, name="ingredient_add"),
    path("recipe/add", recipe_add, name="recipe_add"),
]

