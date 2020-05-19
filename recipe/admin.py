from django.contrib import admin
from .models import Recipe

class RecipeList(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')

admin.site.register(Recipe, RecipeList)
