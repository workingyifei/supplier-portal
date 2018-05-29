from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.


class Audit(models.Model):
    commodity = models.CharField(default="ex. powertrain", max_length=200)
    supplier = models.CharField('supplier name', max_length=200)
    location = models.CharField(default='supplier location', max_length=200)
    contact = models.CharField(default='supplier contact', max_length=200)
    request_date = models.DateTimeField(auto_now=True)
    firstname = models.CharField(default=User.first_name, max_length=200)
    def __str__(self):
        return self.supplier


