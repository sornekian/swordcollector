from django.db import models
from django.urls import reverse

# Create your models here.
class Warrior(models.Model):
    name = models.CharField(max_length=100)
    faction = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('warriors_detail', kwargs={'pk': self.id})

class Swordsmith(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    warriors = models.ManyToManyField(Warrior)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'swordsmith_id': self.id})


class Sword(models.Model): 
    category = models.CharField(max_length=100)   
    age = models.CharField(max_length=100)
    blade_material = models.CharField(max_length=100)
    blade_length = models.DecimalField(max_digits = 5, decimal_places = 2)

    swordsmith = models.ForeignKey(Swordsmith, on_delete=models.CASCADE)