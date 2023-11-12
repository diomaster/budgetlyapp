from django.db import models

# Create your models here.

class AccountInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()

    def str(self):
        return self.username
    


class Category(models.Model):   
    name = models.CharField(max_length=100)

    def str(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    planned = models.FloatField(max_length=15)
    recieved = models.FloatField(max_length=15)

    def str(self):
        return self.name
    

class Transaction(models.Model):        
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField()
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    

    def str(self):
        return self.category