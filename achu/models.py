from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    Price=models.FloatField()
    image=models.CharField(max_length=500)
    def __str__(self):
        return self .name