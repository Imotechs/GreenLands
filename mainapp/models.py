from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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


#trending tocks table
class Trending(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(default = 'media/Trending/default.jpg', upload_to = 'media/Trending')
    local_govt = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    first_quarter = models.BooleanField(default=True)
    second_quarter = models.BooleanField(default=False)    
    quantity = models.IntegerField()
    offer_season = models.CharField(max_length=20)
    offer_gain = models.CharField(max_length=20)
    offer_duration = models.CharField(max_length=20)
    available = models.BooleanField(default=True)
    is_promoted = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)

#farm Tools 
class Farm_Tool(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(default = 'media/Farm_tool/default.jpg', upload_to = 'media/Farm_tool')
    local_govt = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    quantity = models.IntegerField()
    customer_phone = models.CharField(max_length=15)
    customer_name = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=30)
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
    cost = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)

# workers table
class AvailableWorker(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    approved = models.BooleanField(default=False) 
    phone = models.CharField(max_length=15,blank=True)
    id_card  = models.ImageField(default = 'media/Identities/default.jpg', upload_to = 'media/Identities')
    id_number = models.CharField(max_length=30)
    description = models.TextField(default = 'I want to be a worker')  
# jobs table

class AvailableJob(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type_of_work = models.CharField(max_length=30,blank = True)
    local_govt = models.CharField(max_length=20,blank = True)
    state = models.CharField(max_length=20,blank = True)
    country = models.CharField(max_length=20,blank = True)
    number_of_workers = models.IntegerField()
    photo = models.ImageField(default = 'media/Jobs/default.jpg', upload_to = 'media/Jobs')
    description = models.TextField(default= 'I have a Job') 
    cost = models.IntegerField()
    available = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
