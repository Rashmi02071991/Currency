# Create your models here.
from django.db import models
from datetime import datetime

from django.db.models.base import Model
from django.db.models.enums import IntegerChoices
# Create your models here.
class Bank(models.Model):
    customer_account_no= models.IntegerField(default=0)
    customer_name = models.CharField(max_length=30)
    type_account = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=500)
    contact_no= models.IntegerField(default=0)
    date= models.DateField(default=datetime.now)
    Image= models.ImageField(upload_to='currencyconverter/images',default="")
    amount= models.IntegerField(default=0)

def __str__(self):
    return self.customer_name

class Transaction(models.Model):
    account_no=models.IntegerField(default=0)
    amount=models.IntegerField(default=0)
    transaction_no=models.IntegerField(default=0)
    satus=models.CharField(max_length=15)
    tdate=models.DateField(default=datetime.now)

def __int__(self):
    return self.account_no


# choices=INTEGER_CHOICES = [('', '')]

# class CurrencyForm(models.Model):
    source_currency_value =models.DecimalField(name='Amount',blank=True, null=True, max_digits=10, decimal_places=10)
    source_currency_code = models.CharField(max_length=200,name='From', choices = INTEGER_CHOICES)
    target_currency_code = models.CharField(max_length=200,name='To',choices=INTEGER_CHOICES)


    def __init__(self, tuple_country_code, *args, **kwargs):
        # required to set the initial form drop down with choices
        self.tuple_country_code = tuple_country_code
        super(CurrencyForm,self).__init__(*args, **kwargs)

        self.fields['source_currency_code'].widget.choices = self.tuple_country_code
        self.fields['target_currency_code'].widget.choices = self.tuple_country_code