from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Dessert', 'Dessert'),
        ('Main Course', 'Main Course'),
        ('Appetizer', 'Appetizer'),
        ('Beverage', 'Beverage'),
        ('Snack', 'Snack'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=30, null=False,blank=False)
    description = models.TextField(max_length=50, null=True)
    instructions = models.TextField(null=False, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)
    preparation_time = models.IntegerField(
        validators=[MinValueValidator(1)],  # Must be at least 1 minute
        help_text="Time in minutes",
        null=True, blank=True
    )
    cooking_time = models.IntegerField(
        validators=[MinValueValidator(1)],  # Must be at least 1 minute
        help_text="Time in minutes",
        null=True, blank=True
    )
    servings = models.IntegerField(
        validators=[MinValueValidator(1)],  # At least 1 serving
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class User(models.Model):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username



class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    required_ingredients = models.TextField(max_length=5000, null=True, blank=True)
    

    def __str__(self):
        return f"{self.name}, ({self.quantity})"
 
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    ratings = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=False, blank=False
    )
    comment = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reviewed by {self.user.username} on {self.recipe.title}"

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(ratings__gte=1) & models.Q(ratings__lte=5),
                                   name="ratings_between_1_and_5")
        ]

