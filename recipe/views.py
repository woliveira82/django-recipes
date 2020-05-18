from django.shortcuts import render
# Create your views here.

def index(request):
    recipe_list = [
        {'recipe_name':'Recipe 01'},
        {'recipe_name':'Recipe 02'},
        {'recipe_name':'Recipe 03'},
    ]
    data = {
        'best_recipe': recipe_list
    }
    return render(request, 'index.html', data)


def recipe(request):
    return render(request, 'recipe.html')
