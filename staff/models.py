from django.db import models
class staff(models.Model):
    name=models.CharField(max_length=100)

    address=models.CharField(max_length=2500)
    mobileno=models.IntegerField()
    image=models.CharField(max_length=5000)


# Create your models here.
