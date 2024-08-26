from django.db import models

# Create your models here.


class Food(models.Model):
    def __str__(self):
        return self.name 
    name = models.CharField(max_length=100,null=False)
    protein = models.FloatField(null= False)
    carb = models.FloatField(null= False)
    fat = models.FloatField(null= False)
    cal = models.IntegerField(null= False)
    category = models.CharField(max_length=100,null=False)