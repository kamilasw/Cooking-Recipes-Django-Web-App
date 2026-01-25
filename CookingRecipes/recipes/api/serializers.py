from rest_framework import serializers
from recipes.models import Ingredient, RecipeIngredient, Recipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id","name"]

class CreateIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["name"]

    def validate_name(self,value):
        value = value.strip()
        if len(value)<3:
            raise serializers.ValidationError("Ingredient name is too short")
        return value

class AddRecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())

    class Meta:
        model = RecipeIngredient
        fields = ["id","ingredient","amount","unit"]

    def validate_amount(self,value):
        if value <=0:
            raise serializers.ValidationError("Amount must be greater than 0")
        return value

class RecipeIngredientOutSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ["id","amount","unit","ingredient"]