from django.urls import path
from .views import recipe_detail,recipe_list
urlpatterns = [
    path('list/', recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]

# This might be needed, depending on your Django version 
app_name = "ledger"
