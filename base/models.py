from django.db import models
import datetime

# Create your models here.

class Order(models.Model):    

    mrr_date=models.DateField() 
    mrr_no=models.CharField(max_length=100, unique=True, null=True) 
    
    def __str__(self):
        return self.mrr_no  

    @property
    def kits(self):
        return self.kit_set.all()    
    

class Kit(models.Model):   

    Model=models.CharField(max_length=100, null=True)
    Body=models.CharField(max_length=100, null=True)
    Lot_No=models.CharField(max_length=100, null=True)
    Variant=models.CharField(max_length=100, null=True)
    Order=models.ForeignKey(Order,on_delete=models.CASCADE)  
    
    VIN=models.CharField(max_length=100, null=True)
    Color=models.CharField(max_length=100, null=True)
    Fuel=models.CharField(max_length=100, null=True)
    Status=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Model  

        
#columns to be added 
# interior color code, interior color, exterior color code, exterior color, OCN number.     