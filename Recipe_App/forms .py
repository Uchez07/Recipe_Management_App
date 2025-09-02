from django import forms
from .models import Recipe, Ingredients

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name', 'quantity', 'unit']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']  # Adjust fields based on your model
