from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from recipes.models import Ingredient, RecipeIngredient, Recipe
from django.db import IntegrityError

from .serializers import (
CreateIngredientSerializer,
IngredientSerializer,
AddRecipeIngredientSerializer,
RecipeIngredientOutSerializer,
)

class IngredientCreateApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        ser = CreateIngredientSerializer(data=request.data)

        if not ser.is_valid():
            msg = ser.errors.get("name", ["Invalid data"])[0]
            return Response({"error": msg}, status=status.HTTP_400_BAD_REQUEST)

        name = ser.validated_data["name"]
        obj, created = Ingredient.objects.get_or_create(name__iexact=name, defaults={"name": name})
        return Response({**IngredientSerializer(obj).data,"created":created}, status=status.HTTP_201_CREATED)

class RecipeIngredientAddApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,pk):
        recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
        ser = AddRecipeIngredientSerializer(data=request.data)

        if not ser.is_valid():
            first_key = next(iter(ser.errors.keys()))
            msg = ser.errors[first_key][0]
            return Response({"error": msg}, status=status.HTTP_400_BAD_REQUEST)

        try:

            ri = RecipeIngredient.objects.create(
                recipe = recipe,
                ingredient=ser.validated_data["ingredient"],
                amount = ser.validated_data["amount"],
                unit = ser.validated_data["unit"],
                )
        except IntegrityError:
            return Response({"error": "this ingredient is already added"}, status=400)

        return Response(RecipeIngredientOutSerializer(ri).data, status=status.HTTP_201_CREATED)






