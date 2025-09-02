from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Recipe, Ingredients, Review
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import IsOwnerOrReadOnly, IsRecipeOwner, IsReviewOwner
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import RecipeForm, IngredientForm, ReviewForm
from . import views


def base(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

# Login View
class UserLoginView(LoginView):
    template_name = 'auth/login.html'  # Create this template
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('recipe-list')  # Redirect after successful login


# Logout View
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect after logout

# Create Recipe
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# List Recipes

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"
    
# Retrieve Single Recipe
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"

# Update Recipe
class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        if form.instance.user != self.request.user:
            form.add_error(None, "You cannot edit this recipe.")
            return self.form_invalid(form)
        return super().form_valid(form)

# Delete Recipe
class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/recipe_confirm_delete.html"
    success_url = reverse_lazy('recipe_list')

# Create Ingredient
class IngredientCreateView(CreateView):
    model = Ingredients
    form_class = IngredientForm
    template_name = "ingredients/ingredient_form.html"

    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        form.instance.recipe = recipe
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ingredient_list', kwargs={'recipe_id': self.kwargs['recipe_id']})


# List Ingredients for a Recipe
class IngredientListView(ListView):
    model = Ingredients
    template_name = "ingredients/ingredient_list.html"
    context_object_name = "ingredients"

    def get_queryset(self):
        recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        return Ingredients.objects.filter(recipe=recipe)


# Update Ingredient
class IngredientUpdateView(UpdateView):
    model = Ingredients
    form_class = IngredientForm
    template_name = "ingredients/ingredient_form.html"

    def get_success_url(self):
        recipe_id = self.object.recipe.id
        return reverse_lazy('ingredient_list', kwargs={'recipe_id': recipe_id})


# Delete Ingredient
class IngredientDeleteView(DeleteView):
    model = Ingredients
    template_name = "ingredients/ingredient_confirm_delete.html"

    def get_success_url(self):
        recipe_id = self.object.recipe.id
        return reverse_lazy('ingredient_list', kwargs={'recipe_id': recipe_id})

# Create Review
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"

    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        form.instance.recipe = recipe
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('review_list', kwargs={'recipe_id': self.kwargs['recipe_id']})


# List Reviews for a Recipe
class ReviewListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    context_object_name = "reviews"

    def get_queryset(self):
        recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        return Review.objects.filter(recipe=recipe)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe_id"] = self.kwargs['recipe_id']
        return context


# Update Review
class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"

    def get_success_url(self):
        return reverse_lazy('review_list', kwargs={'recipe_id': self.object.recipe.id})


# Delete Review
class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "reviews/review_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('review_list', kwargs={'recipe_id': self.object.recipe.id})