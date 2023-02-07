from django.db import models
from django.urls import reverse

# Create your models here.
class Sword(models.Model):
    category = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    swordsmith = models.CharField(max_length=100)
    blade_material = models.CharField(max_length=100)
    blade_length = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'sword_id': self.id})