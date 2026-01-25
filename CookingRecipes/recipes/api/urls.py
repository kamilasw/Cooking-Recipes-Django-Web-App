from django.urls import path
from .views import IngredientCreateApi, RecipeIngredientAddApi

urlpatterns = [
    path("ingredients/", IngredientCreateApi.as_view(),name="api_create_ingredient"),
    path("recipes/<int:pk>/ingredients/",RecipeIngredientAddApi.as_view(),name="api_add_ingredient_to_recipe"),
]