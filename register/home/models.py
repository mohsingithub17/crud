from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    number=models.CharField(max_length=10)
    password=models.CharField(max_length=500, blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    
    
    
