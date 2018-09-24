from django.contrib import admin
from .models import Car, Fuel, Service, Mileage

admin.site.register(Car)
admin.site.register(Fuel)
admin.site.register(Service)
admin.site.register(Mileage)
