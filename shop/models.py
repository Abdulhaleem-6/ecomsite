from django.db import models

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length= 200)
    price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.CharField(max_length= 200)
    description = models.TextField()
    image = models.CharField(max_length= 2000)

class Orders(models.Model):
    def __str__(self) -> str:
        return self.name
    
    items = models.CharField(max_length=2000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)