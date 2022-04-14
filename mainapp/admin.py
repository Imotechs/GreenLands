from django.contrib import admin
from .models import Profile,Crop,Advert,AvailableJob,AvailableWorker,Land,Trending,Farm_Tool
# Register your models here.
admin.site.register(Profile)
admin.site.register(Crop)
admin.site.register(AvailableJob)
admin.site.register(Advert)
admin.site.register(AvailableWorker)
admin.site.register(Land)
admin.site.register(Trending)
admin.site.register(Farm_Tool)