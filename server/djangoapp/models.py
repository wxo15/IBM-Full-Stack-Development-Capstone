from django.db import models
from django.utils.timezone import now


class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description

class CarModel(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(null=False)
    name = models.CharField(null=False, max_length=50)
    year = models.DateField()

    SUV = 'SUV'
    SEDAN = 'Sedan'
    WAGON = 'WAGON'

    TYPES = [
        (SUV, 'suv'),
        (SEDAN, 'sedan'),
        (WAGON, 'wagon'),
    ]

    type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPES,
        default=SEDAN
    )

    def __str__(self):
        return self.make.name + " " + \
               self.name + ", " + \
               str(self.year.year) + "(" + \
               "DealerID: " + str(self.dealer_id) + ")"


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
