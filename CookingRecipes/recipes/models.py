from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MinLengthValidator


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(validators=[MinLengthValidator(3)], max_length=200)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    prep_time = models.PositiveIntegerField(validators=[MinValueValidator(1)]) #time must be >=1 (minutes)
    is_public = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipes')
    def __str__(self) -> str: return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=120, unique=True ,validators=[MinLengthValidator(3)])
    def __str__(self) -> str: return self.name
    def save(self, *args, **kwargs):
        self.name=self.name.lower()  # all ingredients must be lowercase
        super().save(*args, **kwargs)


class Unit(models.TextChoices):
    KG = 'kg', 'kg'
    G = 'g', 'g' # gram
    ML = 'ml', 'ml'
    TSP = 'tsp', 'tsp'
    TBSP = 'tbsp', 'tbsp'
    CUP = 'cup', 'cup'

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_recipes')
    amount = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)]) # must be >0
    unit = models.CharField(choices=Unit.choices, default=Unit.G, max_length=10)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['recipe', 'ingredient'], name='unique_ingredient_recipe'),
        ]
    def __str__(self) -> str: return f"{self.amount} {self.unit} {self.ingredient.name}"


