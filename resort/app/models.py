from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class CustomerModel(models.Model):
    name=models.CharField(max_length=100,default=' ')
    contact=PhoneNumberField(region='NP')
    arrivals=models.CharField(max_length=200,default=" ")
    departure=models.CharField(max_length=100,default=' ')
    pax=models.CharField(max_length=100,default=' ')
    stay_type=models.CharField(max_length=100,default=' ')
    package=models.CharField(max_length=200,default=' ')
    tariff=models.CharField(max_length=100,default=' ')
    advance=models.IntegerField(default=0)
    remarks=models.TextField()

    def __str__(self):
        return self.name