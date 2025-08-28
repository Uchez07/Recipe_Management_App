from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Recipe, Ingredients, Review
from .serializers import RecipeSerializer, IngredientSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly, IsRecipeOwner, IsReviewOwner

# Create Recipe
class RecipeCreateView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# List Recipes
class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Retrieve Single Recipe
class RecipeDetailView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Update Recipe
class RecipeUpdateView(generics.UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]

# Delete Recipe
class RecipeDeleteView(generics.DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]

# Create Ingredient
class IngredientCreateView(generics.CreateAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        recipe_id = self.kwargs.get('recipe_id')
        serializer.save(recipe_id=recipe_id)

# List Ingredients for a Recipe
class IngredientListView(generics.ListAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        recipe_id = self.kwargs.get('recipe_id')
        return Ingredients.objects.filter(recipe_id=recipe_id)

# Update Ingredient
class IngredientUpdateView(generics.UpdateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsRecipeOwner]

# Delete Ingredient
class IngredientDeleteView(generics.DestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsRecipeOwner]

# Create Review
class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        recipe_id = self.kwargs.get('recipe_id')
        serializer.save(user=self.request.user, recipe_id=recipe_id)

# List Reviews for a Recipe
class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        recipe_id = self.kwargs.get('recipe_id')
        return Review.objects.filter(recipe_id=recipe_id)

# Update Review
class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewOwner]

# Delete Review
class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewOwner]

    