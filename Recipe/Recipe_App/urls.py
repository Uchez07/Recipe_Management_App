# recipe_app/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    RecipeCreateView, RecipeListView, RecipeDetailView, RecipeUpdateView, RecipeDeleteView, 
    IngredientCreateView, IngredientListView, IngredientUpdateView, IngredientDeleteView,
    ReviewCreateView, ReviewListView, ReviewUpdateView, ReviewDeleteView,
    UserLoginView, UserLlogoutView)

urlpatterns = [
    path('', views.base, name='base'),
    path('home', veiws.home, name='home'),

    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),

     # Ingredients
    path('recipes/<int:recipe_id>/ingredients/', IngredientListView.as_view(), name='ingredient-list'),
    path('recipes/<int:recipe_id>/ingredients/create/', IngredientCreateView.as_view(), name='ingredient-create'),
    path('ingredients/<int:pk>/update/', IngredientUpdateView.as_view(), name='ingredient-update'),
    path('ingredients/<int:pk>/delete/', IngredientDeleteView.as_view(), name='ingredient-delete'),

    # Reviews
    path('recipes/<int:recipe_id>/reviews/', ReviewListView.as_view(), name='review-list'),
    path('recipes/<int:recipe_id>/reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
]
