from django.urls import path
from recipes.views import show_recipe, recipe_list

urlpatterns = [
    path("recipes/", recipe_list),
    path("recipes/<int:id>/", show_recipe),
]