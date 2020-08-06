from django.db import models

# Create your models here.

class all_results(models.Model):
    computer= models.CharField(max_length=100)
    person= models.CharField(max_length=100)
    result= models.CharField(max_length=100)