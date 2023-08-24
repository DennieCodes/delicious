from django.shortcuts import render, get_object_or_404
from recipes.models import Recipe

def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe
    }
    return render(request, "recipes/detail.html", context)