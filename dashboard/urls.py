from django.urls import path
from .views import Dashboard,Emails,MakeMail,SharePayment,FarmPayment,AllUsers,Workers,AddStaff

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('mails/', Emails.as_view(), name = 'mails'),
    path('compose/mails/', MakeMail.as_view(), name = 'makemail'),
    path('all/shares/payments/', SharePayment.as_view(), name = 'allshares'),
    path('all/farm/payments/', FarmPayment.as_view(), name = 'allfarms'),
    path('all/users/accounts/', AllUsers.as_view(), name = 'allusers'),
    path('all/availble/workers/', Workers.as_view(), name = 'allworkers'),
    path('add/staff/<int:pk>/', AddStaff.as_view(), name = 'addstaff'),


]