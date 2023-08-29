from django.urls import path
from recipes.views import show_recipe, recipe_list, create_recipe, edit_recipe

urlpatterns = [
    path("", recipe_list, name="recipe_list"),
    path("<int:id>/", show_recipe, name="show_recipe"),
    path("<int:id>/edit", edit_recipe, name="edit_recipe"),
    path("create/", create_recipe, name="create_recipe")
]