from django.contrib import admin
from .models import FarmImpliments, Shares, Profile,Crop,Advert,AvailableJob,AvailableWorker,Land,GreenlandFarms,FarmImpliments
# Register your models here.
admin.site.register(Profile)
admin.site.register(Crop)
admin.site.register(AvailableJob)
admin.site.register(Advert)
admin.site.register(AvailableWorker)
admin.site.register(Land)
admin.site.register(GreenlandFarms)
admin.site.register(FarmImpliments)
admin.site.register(Shares)