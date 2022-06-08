from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    count = models.IntegerField()
    comment = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    

class Review(models.Model):
    pro = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    con = models.TextField()
    
    def __str__(self) -> str:        
        return f"{self.pro.name}_{self.name}"
    