from django.urls import path
from recipes.views import show_recipe, recipe_list, create_recipe

urlpatterns = [
    path("recipes/", recipe_list, name="recipe_list"),
    path("recipes/<int:id>/", show_recipe, name="show_recipe"),
    path("recipes/create", create_recipe, name="create_recipe")
]