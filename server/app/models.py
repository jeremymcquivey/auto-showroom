from django.db import models

# Create your models here.
class Car(models.Model):

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    year = models.SmallIntegerField()
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    sub = models.CharField(max_length=20)