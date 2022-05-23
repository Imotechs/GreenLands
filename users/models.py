from django.db import models
from django.contrib.auth.models import User
from mainapp.models import *
# Create your models here.
class Mail(models.Model):
    your_name = models.CharField(max_length=30, blank = True)
    email_address = models.CharField(max_length=30,blank = True)
    phone_number=models.CharField(max_length=30,blank = True)
    how_can_we_help_you = models.TextField(blank = True) 
    seen = models.BooleanField(default=False)

class UserAdress(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    detail_address = models.TextField(blank=True)

class LandRequest(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=15)
    customer_mail = models.CharField(max_length=30)
    customer_message = models.TextField()
    is_approved = models.BooleanField(default=False)



class FarmsPayment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    farm = models.ForeignKey(GreenlandFarms,on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=20, blank=True)
    cost = models.DecimalField(max_digits=100, decimal_places=3)
    is_id = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user}'s {self.farm} payment"

class SharesPayment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=10)
    work_status = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    id_number = models.CharField(max_length=25)
    id_type = models.CharField(max_length=15)
    DOBd = models.CharField(max_length=4)
    DOBm = models.CharField(max_length=5)
    DOBy = models.CharField(max_length=5)
    gender = models.CharField(max_length=15)
    country = models.CharField(max_length=15, blank=True)
    payment_method = models.CharField(max_length=15)
    acc_number = models.CharField(max_length=15)
    bank = models.CharField(max_length=15)
    acc_type = models.CharField(max_length=15)
    shares = models.ForeignKey(Shares, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=20, blank=True)
    cost = models.DecimalField(max_digits=100, decimal_places=3)
    is_id = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)