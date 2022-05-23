from django.contrib import admin
from .models import Mail,UserAdress,LandRequest,FarmsPayment, SharesPayment
# Register your models here.
admin.site.register(Mail)
admin.site.register(UserAdress)
admin.site.register(LandRequest)
admin.site.register(FarmsPayment)
admin.site.register(SharesPayment)