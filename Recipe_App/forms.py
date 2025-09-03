from django import forms
from .models import Recipe, Ingredients, Review

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
