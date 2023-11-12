from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()