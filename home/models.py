from django.db import models

# Create your models here.

class Listed_Cars(models.Model):
    email = models.EmailField()
    list_car_name = models.CharField(max_length=200)
    list_price = models.IntegerField()
    list_km_driven = models.IntegerField()
    list_owners_count = models.IntegerField()
    list_year = models.IntegerField()
    list_fuel_type = models.CharField(max_length=200)
    list_transmission_type = models.CharField(max_length=200)
    list_phone_number = models.IntegerField()
    list_seller_name = models.CharField(max_length=200)
    list_city = models.CharField(max_length=200)
    list_number_plate = models.CharField(max_length=200)

    def __str__(self):
        return (f"{self.list_car_name} ({self.list_year}) - {self.list_fuel_type} - {self.list_transmission_type}  - {self.email}")

class Data_set(models.Model):
    car_name = models.CharField(max_length=200)
    year = models.IntegerField()
    selling_price = models.FloatField()
    present_price = models.FloatField()
    kms_driven = models.IntegerField()
    fuel_type = models.IntegerField()
    seller_type = models.IntegerField()
    transmission = models.IntegerField()
    owners = models.IntegerField()

    def __str__(self):

        fuel=""
        transmit_type=""

        if(self.fuel_type==0):
            fuel="Petrol"
        elif(self.fuel_type==1):
            fuel="Diesel"
        elif(self.fuel_type==2):
            fuel="CNG"
        elif(self.fuel_type==3):
            fuel="LPG"

        if(self.transmission==0):
            transmit_type="Manual"
        elif(self.transmission==1):
            transmit_type="Automatic"
        
        
        return (f"{self.car_name} ({self.year}) - {fuel} - {transmit_type}")
    