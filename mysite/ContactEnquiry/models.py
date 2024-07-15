from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=15)
    referral = models.CharField(max_length=100)
    date = models.DateField()
    occassion = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    CURRENCY_CHOICES = (('INR','Indian Rupee'),('USD','US Dollar'))
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='INR')
    budget = models.CharField(max_length=100)
    comments = models.TextField()