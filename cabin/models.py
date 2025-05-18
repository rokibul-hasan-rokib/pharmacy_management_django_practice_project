from django.db import models

class Cabin(models.Model):
    CABIN_TYPE_CHOICES = [
        (1, 'Economy'),
        (2, 'Deluxe'),
        (3, 'Suite'),
    ]

    cabin_number = models.CharField(max_length=100)
    cabin_type = models.PositiveSmallIntegerField(choices=CABIN_TYPE_CHOICES)
    cabin_price = models.CharField(max_length=100)

    class Meta:
        db_table = 'cabins'

    def __str__(self):
        return self.cabin_number

