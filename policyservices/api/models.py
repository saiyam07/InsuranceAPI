'''
models are registered here
'''
from django.db import models


#class to define the choices a column could have
class YesNo(models.IntegerChoices):
    '''
    Defines Integer choices for the attribute
    Yes for 1
    No for 0
    '''
    YES= 1
    NO = 0

class Customer(models.Model):
    '''
    Customer Model Defination
    <PK>:CustomerId
    '''
    customerId = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=7)
    incomeGroup = models.CharField(max_length=30)
    region = models.CharField(max_length=10)
    marital_status = models.IntegerField(choices=YesNo.choices)

    def __str__(self):
        return str(self.customerId)



class Policy(models.Model):
    '''
    Policy Model Defination
    <PK>:policyID
    <FK>:customer refrences Customer Model
    '''
    policyId = models.AutoField(primary_key=True)
    purchaseDate = models.DateField()
    fuel = models.CharField(max_length=10)
    vehicleSegment = models.CharField(max_length=1)
    premium = models.DecimalField(max_digits=7,decimal_places=0)
    bodilyInjuryLiability = models.IntegerField(choices=YesNo.choices)
    personalInjuryProtection = models.IntegerField(choices=YesNo.choices)
    propertyDamageLiability = models.IntegerField(choices=YesNo.choices)
    collision = models.IntegerField(choices=YesNo.choices)
    comprehensive = models.IntegerField(choices=YesNo.choices)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.policyId)
