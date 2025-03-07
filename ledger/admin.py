from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name',)  

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ('ingredient', 'recipe', 'quantity') 

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)