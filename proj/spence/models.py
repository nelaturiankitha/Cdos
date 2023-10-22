# from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class Spence(models.Model):
# each class variable represents a database i.e. table field in the model
    item = models.CharField(max_length=200)
    cost = models.CharField(max_length=30)
    expiry_date = models.DateTimeField('release date')
    quantity = models.IntegerField()
    duration = models.FloatField()
    
    def __str__(self):
        return self.item + " - " + self.cost
        