from django.db import models

# Create your models here.

class things(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quanity=models.IntegerField()
    def __str__(self):
        return self.name
