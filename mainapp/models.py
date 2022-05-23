from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(default = 'media/user_profiles/default.PNG', upload_to = 'media/user_profiles')
    phone = models.CharField(max_length=15)
    date_added = models.DateTimeField(auto_now=True)
    def save(self):
        super().save()
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width >300:
            imageparam = (200, 200)
            img.thumbnail(imageparam)
            img.save(self.photo.path)
        if img.height < 300 or img.width < 300:
            imageparam = (200, 200)
            img.thumbnail(imageparam)
            img.save(self.photo.path)

class Crop(models.Model):
    name = models.CharField(max_length=10)
    photo = models.ImageField(default = 'media/crops/default.jpg', upload_to = 'media/crops')
    date_added = models.DateTimeField(auto_now=True)
    def save(self):
        super().save()
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width >300:
            imageparam = (300, 300)
            img.thumbnail(imageparam)
            img.save(self.photo.path)
        if img.height < 300 or img.width < 300:
            imageparam = (300, 300)
            img.thumbnail(imageparam)
            img.save(self.photo.path)

class Advert(models.Model):
    name = models.CharField(max_length=15)
    photo = models.ImageField(default = 'media/Adverts/default.jpg', upload_to = 'media/Adverts')
    descriptions = models.TextField()
    date_added = models.DateTimeField(auto_now=True)


#GreenlandFarms tocks table
class GreenlandFarms(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(default = 'media/GreenlandFarms/default.jpg', upload_to = 'media/GreenlandFarms')
    local_govt = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    first_quarter = models.BooleanField(default=True)
    second_quarter = models.BooleanField(default=False)    
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=3)
    offer_season = models.CharField(max_length=20)
    offer_gain = models.CharField(max_length=20)
    offer_duration = models.CharField(max_length=20)
    available = models.BooleanField(default=True)
    is_promoted = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    description = models.TextField(default='A new farm')

#farm Tools 
class FarmImpliments(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(default = 'media/FarmImpliments/default.jpg', upload_to = 'media/FarmImpliments')
    local_govt = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    quantity = models.IntegerField()
    customer_phone = models.CharField(max_length=15)
    customer_name = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=150)
    description = models.TextField(default='All available Tool at Greenlands')
    date_added = models.DateTimeField(auto_now=True)

#Land for rent Table

class Land(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(default = 'media/Land/default.jpg', upload_to = 'media/Land')
    local_govt = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    quantity = models.IntegerField()
    customer_phone = models.CharField(max_length=15)
    available = models.BooleanField(default=True)
    description = models.TextField(default='A new Land')
    cost = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)

# workers table
class AvailableWorker(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    local_govt = models.CharField(max_length=20,blank = True)
    state = models.CharField(max_length=20,blank = True)
    country = models.CharField(max_length=20,blank = True)
    type_of_work = models.CharField(max_length=30,blank = True)
    upfront = models.CharField(max_length=30,blank = True)
    phone = models.CharField(max_length=15,blank=True)
    id_card  = models.ImageField(default = 'media/Identities/default.jpg', upload_to = 'media/Identities')
    id_number = models.CharField(max_length=30)
    description = models.TextField(default = 'I want to be a worker... i do this, i do that ... etc')  
    approved = models.BooleanField(default=False) 

# jobs table

class AvailableJob(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type_of_work = models.CharField(max_length=30,blank = True)
    local_govt = models.CharField(max_length=20,blank = True)
    state = models.CharField(max_length=20,blank = True)
    country = models.CharField(max_length=20,blank = True)
    number_of_workers = models.IntegerField()
    description = models.TextField(default= 'I have a Job,(1) to do this...(2) to do that ...(...)') 
    cost = models.IntegerField()
    available = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return (f"{self.user}'s Job")
    def get_absolute_url(self):
        return reverse('jobdetail',kwargs = {'pk':self.pk })
    
class Shares(models.Model):
    name = models.CharField(max_length=15)
    cost = models.DecimalField(max_digits=100, decimal_places=3)
    offer_gain = models.TextField(default= 'Get up to so...so.percent return investing in so..so Shares')
    description = models.TextField(default= 'Buy Greenland shares with a minimum of $50 and get 80 - 100 return in a Year') 
    min_cost = models.DecimalField(max_digits=100, decimal_places=3)
    max_cost = models.DecimalField(max_digits=100, decimal_places=3)
    date_added = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name}"
