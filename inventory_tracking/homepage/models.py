from django.db import models
from polymorphic.models import PolymorphicModel
import random
import string

# Create your models here.

class Location(models.Model):
    #id
    city2 = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    zipcode = models.IntegerField(default=11111)

class Product(PolymorphicModel):
    #id
    location = models.ForeignKey('Location')
    org_tag = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    manufacturer = models.TextField(blank=True, null=False)
    man_part_number = models.IntegerField(default=1234)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    man_notes = models.TextField(blank=True, null=True)
