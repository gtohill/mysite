from django.db import models

# Create your models here.


class Register(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.name
