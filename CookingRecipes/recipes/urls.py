from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="public_recipe_list", permanent=False)),
    path("recipes/", views.public_recipe_list, name="public_recipe_list"),
    path("recipes/<int:pk>/", views.public_recipe_detail, name="public_recipe_detail"),
    path("my/recipes/",views.my_recipe_list, name="my_recipe_list"),
    path("my/recipes/<int:pk>/",views.my_recipe_detail, name="my_recipe_detail"),
    path("my/recipes/new/",views.my_recipe_new, name="my_recipe_new"),
    path("my/recipes/<int:pk>/edit/",views.my_recipe_edit, name="my_recipe_edit"),
    path("my/recipes/<int:pk>/delete/",views.my_recipe_delete, name="my_recipe_delete"),
    path("/ingredients/", views.create_ingredient, name="create_ingredient"),
    path("/recipes/<int:pk>/ingredients/",views.add_ingredient_to_recipe, name="add_ingredient_to_recipe"),
]