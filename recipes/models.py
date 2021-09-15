from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    instructions = models.TextField()

class RecipeIngredient(models.Model):
    class Units(models.TextChoices):
        GRAM = 'G', 'Gram'
        KILOGRAM = 'KG', 'Kilogram'
        INCH = 'IN', 'Inch'
        TABLESPOON = 'TBSP', 'Tablespoon'
        TEASPOON = 'TSP', 'Teaspoon'
        CUP = 'CUP', 'Cup'
        OUNCE_VOLUME = 'OZ_V', 'Ounce'
        OUNCE_MASS = 'OZ_M', 'Ounce'

    ingredient = models.ForeignKey(Ingredient)
    quantity = models.DecimalField(max_digits=8, decimal_places=3)
    unit = models.CharField(max_length=4, choices=Units.choices)
    recipe = models.ForeignKey(Recipe)
