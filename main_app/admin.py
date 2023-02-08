from django.contrib import admin
from .models import Swordsmith, Sword, Warrior

# Register your models here.
admin.site.register(Swordsmith)
admin.site.register(Sword)
admin.site.register(Warrior)