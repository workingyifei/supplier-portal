from django.db import models
from datetime import date

# Create your models here.


class Audit(models.Model):
    SYSTEM_CHOICE = (
        ('ADAS', 'ADAS' ),
        ('BIW', 'BIW'),
        ('Chassis', 'Chassis'),
        ('Exterior', 'Exterior'),
        ('Interior', 'Interior'),
        ('Powertrain', 'Powertrain'),
        ('Thermal', 'Thermal'),
        ('LowVoltageEE', 'LowVoltage EE'),
        ('Connectivity', 'Connectivity'),
        ('ICE', "Intelligent Car Experience")
    )

    PRIORITY_CHOICE = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    )
    system = models.CharField(max_length=30, choices=SYSTEM_CHOICE,default='ADAS')
    commodity = models.CharField(default='e.g. Radar', max_length=200)

    # TODO: Pop up a calendar to show month and dates
    audit_before = models.DateField(auto_now=True)

    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICE, default='Low')
    supplier_name = models.CharField(max_length=30)
    supplier_location = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=30)
    contact_email = models.EmailField()
    buyer_first_name = models.CharField(max_length=30)
    buyer_last_name = models.CharField(max_length=30)
    buyer_email = models.EmailField()
    quality_first_name = models.CharField(max_length=30)
    quality_last_name = models.CharField(max_length=30)
    quality_email = models.EmailField()

    def __str__(self):
        return self.commodity + ', ' + self.system

