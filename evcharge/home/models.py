from django.db import models

# Create your models here.

class stationdetails(models.Model):
    name = models.CharField(max_length= 100)
    latitude = models.FloatField(max_length= 200)
    longitude = models.FloatField(max_length= 200)
    chargeprice = models.FloatField(max_length=100)
    charger1 = models.CharField(max_length=50, null=True, blank=True)
    charger2 = models.CharField(max_length=50, null=True, blank=True)
    charger3 = models.CharField(max_length=50, null=True, blank=True)
    charger4 = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=300,default=None, blank=True, null=True)


class reviews(models.Model):
    username = models.CharField(max_length=100)
    stationname = models.CharField(max_length=100)
    highlights = models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.CharField(max_length=800)
    

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = "contact"
