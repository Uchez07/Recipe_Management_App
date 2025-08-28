from django.shortcuts import render
from.models import Recipe, Ingredients, Review
from rest_framework import generics, permissions
from .models import Recipe
from .serializers import RecipeSerializer
from .permissions import IsOwnerOrReadOnly

# List all recipes & create new recipe
class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all().order_by('-created_at')
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # set current user as owner


# Retrieve, update, or delete a specific recipe
class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

