from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, RecipeIngredient, Ingredient
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from django.views.decorators.http import require_POST
from django.contrib import messages
# Create your views here.


# public recipes
def public_recipe_list(request):
    recipes = Recipe.objects.filter(is_public=True).order_by("-id")
    return render(request,"public_list.html",{"recipes":recipes})

def public_recipe_detail(request,pk):
    recipe = get_object_or_404(Recipe,pk=pk, is_public=True)
    ingredients = recipe.recipe_ingredients.select_related("ingredient")
    return render(request,"public_detail.html", {"recipe":recipe, "ingredients":ingredients})

# "my" public and private recipes

@login_required(login_url='/accounts/login/')
def my_recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user).order_by("-id")
    return render(request,"my_list.html",{"recipes":recipes})

@login_required(login_url='/accounts/login/')
def my_recipe_detail(request,pk):
    recipe = get_object_or_404(Recipe,pk=pk,user=request.user)
    ingredients = recipe.recipe_ingredients.select_related("ingredient")
    return render(request, "my_detail.html", {"recipe":recipe, "ingredients":ingredients})

# managing recipes

@login_required(login_url='/accounts/login/')
def my_recipe_new(request):
    if request.method == "POST": # means that form should be filled in
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect("my_recipe_detail", pk=recipe.pk)
        else:
            return redirect("my_recipe_list")
    else: # means the form was only opened now
        form = RecipeForm()
    return render(request,"recipe_form.html",{"form":form,"mode":"create"})


@login_required(login_url='/accounts/login/')
def my_recipe_edit(request,pk):
    recipe = get_object_or_404(Recipe,pk=pk,user=request.user)

    if request.method == "POST":
        form = RecipeForm(request.POST,instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request,"Recipe updated")
            return redirect("my_recipe_detail", pk=recipe.pk)
        else:
            messages.failure(request,"Recipe not updated")
            return redirect("my_recipe_list")
    else:
        form = RecipeForm(instance=recipe)

    ingredients = recipe.recipe_ingredients.select_related("ingredient")

    return render(
        request,
        "recipe_form.html",
        {"form": form, "mode": "edit", "recipe": recipe, "ingredients": ingredients},
    )

@login_required(login_url='/accounts/login/')
@require_POST
def my_recipe_delete(request,pk):
    recipe = get_object_or_404(Recipe,pk=pk,user=request.user)
    recipe.delete()
    messages.success(request,"Recipe deleted")
    return redirect("my_recipe_list")

# AJAX api for ingredient managing

@login_required(login_url='/accounts/login/')
@require_POST
def create_ingredient(request):
    name = (request.POST.get("name") or "").strip()
    if len(name) <3:
        return JsonResponse({"error":"name is too short (min 3 characters)"})
    else:
        ingredient, created = Ingredient.objects.get_or_create(name=name.lower())
        return JsonResponse({"ok": True, "id": ingredient.id, "name": ingredient.name, "created": created})

@login_required(login_url='/accounts/login/')
@require_POST
def add_ingredient_to_recipe(request,pk):
    recipe = get_object_or_404(Recipe,pk=pk,user=request.user)

    ingredient = request.POST.get("ingredient")
    amount = request.POST.get("amount")
    unit = request.POST.get("unit")

    if not ingredient:
        return JsonResponse({"error":"ingredient is required"})
    try:
        ing = RecipeIngredient.objects.create(
            recipe=recipe,
            ingredient=ingredient,
            amount=amount,
            unit=unit
        )
    except IntegrityError:
        return JsonResponse({"error":"this ingredient is already added"})

    return JsonResponse({"ok": True, "ingredient": ing.ingredient, "amount": ing.amount, "unit": ing.unit})