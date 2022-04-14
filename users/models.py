from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Mail(models.Model):
    your_name = models.CharField(max_length=30, blank = True)
    email_address = models.CharField(max_length=30,blank = True)
    phone_number=models.CharField(max_length=30,blank = True)
    how_can_we_help_you = models.TextField(blank = True) 

class UserAdress(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    detail_address = models.TextField(blank=True)