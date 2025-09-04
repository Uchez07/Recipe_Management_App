from rest_framework import generics
from .models import Recipe, Ingredients, Review
from .serializers import RecipeSerializer, IngredientSerializer, ReviewSerializer

# Recipe APIs
class RecipeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# Ingredient APIs
class IngredientListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        recipe_id = self.kwargs['recipe_id']
        return Ingredients.objects.filter(recipe_id=recipe_id)

    def perform_create(self, serializer):
        recipe_id = self.kwargs['recipe_id']
        serializer.save(recipe_id=recipe_id)


class IngredientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer


# Review APIs
class ReviewListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        recipe_id = self.kwargs['recipe_id']
        return Review.objects.filter(recipe_id=recipe_id)

    def perform_create(self, serializer):
        recipe_id = self.kwargs['recipe_id']
        serializer.save(recipe_id=recipe_id)


class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
