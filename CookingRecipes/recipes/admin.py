from django.contrib import admin

from recipes.models import Recipe
from recipes.models import Ingredient
from recipes.models import RecipeIngredient

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
