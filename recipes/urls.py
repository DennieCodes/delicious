from django.urls import path
from recipes.views import show_recipe

urlpatterns = [
    path("recipes/", show_recipe),
]