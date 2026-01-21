from django import forms
from .models import Recipe, RecipeIngredient, Ingredient
from django.forms import modelformset_factory, inlineformset_factory


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name","description","instructions","prep_time","is_public"]
        widgets = {
            "description": forms.Textarea(attrs={"rows":4}),
            "instructions": forms.Textarea(attrs={"rows":4}),
        }
