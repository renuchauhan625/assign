from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=50)
    comname=models.CharField(max_length=200)
    def __str__(self):
        return self.name