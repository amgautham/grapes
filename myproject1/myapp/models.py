from django.db import models

class my_table(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=30)

# Create your models here.
