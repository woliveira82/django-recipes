from django.shortcuts import render, get_object_or_404
from .models import Recipe

def index(request):
    recipe_list = Recipe.objects.all()
    data = {
        'recipe_list': recipe_list
    }
    return render(request, 'index.html', data)


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    data = {
        'recipe': recipe
    }
    return render(request, 'recipe.html', data)
