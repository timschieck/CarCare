import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(default=0)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    miles = models.IntegerField(default=0)
    trim_package = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)
    vin = models.CharField(max_length=17)
    tire_size = models.CharField(max_length=20)
    #add_date = models.DateTimeField('date added')
    def __str__(self):
            return self.name
    def was_added_recently(self):
        return self.add_date >= timezone.now() - datetime.timedelta(days=1)

class Fuel(models.Model):
    date = models.DateField('date added')
    gallons = models.DecimalField(decimal_places=3, max_digits=5)
    cost = models.DecimalField(decimal_places=2, max_digits=5)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

class Service(models.Model):
    date = models.DateField('date added')
    description = models.CharField(max_length=50)
    notes = models.TextField()
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    def __str__(self):
            return self.description

class Mileage(models.Model):
    miles = models.IntegerField(default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField('date added')
