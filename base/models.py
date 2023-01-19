from django.db import models

# Create your models here.


class Wattmeter(models.Model):
    name = models.CharField(max_length=200)
    unkey = models.CharField(max_length=200, unique=True)


class Measure(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.PositiveIntegerField()
    wattmeter = models.ForeignKey(Wattmeter, on_delete=models.CASCADE)
