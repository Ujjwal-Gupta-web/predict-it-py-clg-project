from django.db import models

# Create your models here.

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
    