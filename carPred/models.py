from django.db import models


# Create your models here.
OWNER_CHOICES = (('0', 'First Owner'),('1', 'Second Owner'))
FUEL_CHOICES = (('petrol', 'Petrol'),
                ('diesel', 'Diesel'),
                ('cng', 'Cng'),)

SELLER_CHOICES = (('individual', 'Individual'),
                  ('dealer', 'Dealer'),)

TRANSMISSION_CHOICES = (('automatic', 'Automatic'),
                            ('manual', 'Manual'),)

class Prediction(models.Model):
    year = models.IntegerField(default=2019)
    present_price = models.FloatField()
    kms_driven = models.IntegerField()
    owner = models.CharField(max_length=20, choices=OWNER_CHOICES ,default='First Owner')
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES,default='Petrol')
    seller_type = models.CharField(max_length=40, choices=SELLER_CHOICES, default='Individual')
    transmission = models.CharField(max_length=40, choices=TRANSMISSION_CHOICES, default='Automatic')
    def total_year(self):
        return 2020-self.year

    def __str__(self):
        return f"Car with {self.present_price} Model of {self.year}"