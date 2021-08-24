from django.db import models
from quantityfield.fields import QuantityField

# Create your models here.
class Ingredient(models.Model):
    MEASUREMENT_UNITS = (
        ('V', 'Volume'),
        ('W', 'Weight'),
    )
    name = models.CharField(max_length=200)
    measurement_units = models.CharField(max_length=1, choices=MEASUREMENT_UNITS)

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    quantity = QuantityField('kilogram')

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    instructions = models.TextField()
