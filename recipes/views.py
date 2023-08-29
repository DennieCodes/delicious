from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm

# SHOW_RECIPE
def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }
    return render(request, "recipes/detail.html", context)

# RECIPE_LIST
def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes,
    }
    return render(request, "recipes/list.html", context)

# CREATE_RECIPE
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()

    context = {
        "form": form,
    }

    return render(request, "recipes/create.html", context)