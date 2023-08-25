from django.urls import path
from recipes.views import show_recipe, recipe_list, create_recipe

urlpatterns = [
    path("recipes/", recipe_list),
    path("recipes/<int:id>/", show_recipe),
    path("recipes/create", create_recipe)
]