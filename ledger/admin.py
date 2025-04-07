from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Recipe, RecipeIngredient, Ingredient, Profile, RecipeImage
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

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,] 

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
