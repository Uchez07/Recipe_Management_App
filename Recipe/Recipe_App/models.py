from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=30, null=False)
    description = models.TextField(max_length=50, null=True)
    ingredients = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

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
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, relate_name ='ingeredients')
    name = models.CharField(max_length=500, null=False)
    quantity = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"{self.name}, ({self.quantity})"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, relate_name='reviews')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, relate_name='reviews')
    ratings = models.Integer(null=False)
    comment = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reviewed by {self.user.username} on {self.recipe.title}"

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=1) & models.Q(rating__lte=5),
                                   name="rating_between_1_and_5")
        ]

