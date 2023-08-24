from django.shortcuts import render

def show_recipe(request):
    return render(request, "recipes/detail.html")