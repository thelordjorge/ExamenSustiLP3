from django.db import models

# Create your models here.
class Region(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    image = models.ImageField(default='null')
    cases = models.DateTimeField(auto_now_add=True)
    deaths = models.CharField(max_length=50)
    lethality = models.CharField(max_length=50)


