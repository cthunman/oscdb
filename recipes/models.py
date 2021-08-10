from django.db import models

# Create your models here.
class Ingredient(models.Model):
    MEASUREMENT_UNITS = (
        ('V', 'Volume'),
        ('W', 'Weight'),
    )
    name = models.CharField(max_length=200)
    measurement_units = models.CharField(max_length=1, choices=MEASUREMENT_UNITS)


class Recipe(models.Model):
    name = models.CharField(max_length=200)
