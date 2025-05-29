from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class menuitem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='media')
    price=models.IntegerField(default=100)
    def __str__(self):
        return self.name
class cart(models.Model):
    menu_item = models.ForeignKey(menuitem, on_delete=models.CASCADE)
    number=models.IntegerField(default=1)

class Reservation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.BigIntegerField()
    date1=models.DateField()
    date2=models.DateField()
    guests=models.IntegerField()
    special=models.TextField()
    def __str__(self):
        return self.name

class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    
    def __str__(self):
        return self.name
    
