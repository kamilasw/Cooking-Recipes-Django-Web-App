from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, RecipeIngredient, Ingredient
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Unit
from decimal import Decimal, InvalidOperation
# Create your views here.



# public recipes:
def public_recipe_list(request):
    recipes = Recipe.objects.filter(is_public=True).order_by("-id")

    q = (request.GET.get("q") or "").strip()
    max_time = request.GET.get("max_time")
    ingredient_ids = request.GET.getlist("ingredient")

    if len(q)>=2:
        recipes = recipes.filter(name__icontains=q).order_by("-id")

    if max_time and max_time.isdigit() and int(max_time)>0:
            recipes = recipes.filter(prep_time__lte=max_time).order_by("-id")

    if ingredient_ids:
        for ing_id in ingredient_ids:
            recipes = recipes.filter(recipe_ingredients__ingredient_id=ing_id).order_by("-id")

    ingredients = Ingredient.objects.order_by("name")
    return render(
        request,
        "public_list.html",
        {
            "recipes":recipes,
            "ingredients":ingredients,
            "q":q,
            "max_time":max_time,
            "ingredient_ids":ingredient_ids,}
            )

def public_recipe_detail(request,pk):
    recipe = get_object_or_404(Recipe,pk=pk, is_public=True)
    ingredients = recipe.recipe_ingredients.select_related("ingredient")
    return render(request,"public_detail.html", {"recipe":recipe, "ingredients":ingredients})

# "my" public and private recipes:

@login_required(login_url='/accounts/login/')
def my_recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user).order_by("-id")

    q = (request.GET.get("q") or "").strip()
    max_time = request.GET.get("max_time")
    ingredient_ids = request.GET.getlist("ingredient")

    if len(q) >= 2:
        recipes = recipes.filter(name__icontains=q).order_by("-id")

    if max_time and max_time.isdigit() and int(max_time)>0:
        try:
            recipes = recipes.filter(prep_time__lte=max_time).order_by("-id")
        except ValueError:
            pass

    if ingredient_ids:
        for ing_id in ingredient_ids:
            recipes = recipes.filter(recipe_ingredients__ingredient_id=ing_id).order_by("-id")

    ingredients = Ingredient.objects.order_by("name")

    return render(
        request,
        "my_list.html",
        {
            "recipes":recipes,
            "ingredients":ingredients,
            "q":q,
            "max_time":max_time,
            "ingredient_ids":ingredient_ids,
        })

@login_required(login_url='/accounts/login/')
def my_recipe_detail(request,pk):
    recipe = get_object_or_404(Recipe,pk=pk,user=request.user)
    ingredients = recipe.recipe_ingredients.select_related("ingredient")
    return render(request, "my_detail.html", {"recipe":recipe, "ingredients":ingredients})

# managing recipes

@login_required(login_url='/accounts/login/')
def my_recipe_new(request):
    if request.method == "POST": # means that form should be filled in
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            messages.success(request, "Recipe created")
            return redirect("my_recipe_edit", pk=recipe.pk)
        else:
            messages.success(request, "Recipe not created")
    else: # means the form was only opened now
        form = RecipeForm()
    return render(request,"recipe_form.html",{"form":form,"mode":"create"})


@login_required(login_url='/accounts/login/')
def my_recipe_edit(request,pk):
    recipe = get_object_or_404(Recipe,pk=pk,user=request.user)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES , instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request,"Recipe updated")
            return redirect("my_recipe_detail", pk=recipe.pk)
        else:
            messages.error(request,"Recipe not updated")
    else:
        form = RecipeForm(instance=recipe)

    ingredients = recipe.recipe_ingredients.select_related("ingredient")

    all_ingredients = Ingredient.objects.order_by("name")
    unit_choices= Unit.choices

    return render(
        request,
        "recipe_form.html",
        {
            "form": form,
            "mode": "edit",
            "recipe": recipe,
            "ingredients": ingredients,
            "all_ingredients":all_ingredients,
            "unit_choices":unit_choices,
        },
    )

@login_required(login_url='/accounts/login/')
@require_POST
def my_recipe_delete(request,pk):
    recipe = get_object_or_404(Recipe,pk=pk,user=request.user)
    recipe.delete()
    messages.success(request,"Recipe deleted")
    return redirect("my_recipe_list")

# AJAX api for ingredient managing (i dont use it cuz i rewrote it for the API requirement, it's in the api folder):

@login_required(login_url='/accounts/login/')
@require_POST
def create_ingredient(request):
    name = (request.POST.get("name") or "").strip()
    if len(name) <3:
        return JsonResponse({"ok":False,"error":"name is too short (min 3 characters)"}, status=400)
    else:
        ingredient, created = Ingredient.objects.get_or_create(name=name.lower())


        return JsonResponse({"ok": True, "id": ingredient.id, "name": ingredient.name, "created": created})

@login_required(login_url='/accounts/login/')
@require_POST
def add_ingredient_to_recipe(request,pk):
    recipe = get_object_or_404(Recipe,pk=pk,user=request.user)

    ingredient_id = request.POST.get("ingredient")

    if not ingredient_id:
        return JsonResponse({
            "ok": False,
            "error": "ingredient is required"},
        status=400)

    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    amount = request.POST.get("amount")
    unit = (request.POST.get("unit") or "").strip()
    valid_units = {v for (v,_) in Unit.choices}
    if unit not in valid_units:
        return JsonResponse({"ok": False, "error": "invalid unit"},status=400)

    try:
        amount = Decimal(amount)
        if amount <= 0:
            raise InvalidOperation()
    except(InvalidOperation,TypeError,ValueError):
        return JsonResponse({"ok": False, "error": "invalid amount"},status=400)


    try:

        ri = RecipeIngredient.objects.create(
            recipe=recipe,
            ingredient=ingredient,
            amount=amount,
            unit=unit
        )
    except IntegrityError:
        return JsonResponse({
            "ok":False,
            "error":"this ingredient is already added"},status=400)

    return JsonResponse({
        "ok": True,
        "ri_id":ri.id,
        "ingredient": {
            "id":ingredient.id,
            "name":ingredient.name,
        },
        "amount": str(ri.amount),
        "unit": ri.unit
    })

