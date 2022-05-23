from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from users.models import FarmsPayment, SharesPayment,Mail
from mainapp.models import AvailableWorker, Shares

from django.contrib import messages
from email.message import EmailMessage
import smtplib
from django.conf import settings

mail_username = settings.EMAIL_HOST_USER
mail_password = settings.EMAIL_HOST_PASSWORD
# Create your views here.


class Dashboard(LoginRequiredMixin,UserPassesTestMixin,TemplateView):
  model = User
  template_name = 'dashboard/index.html'

  def get_context_data(self, *args, **kwargs):
    context =super(Dashboard,self).get_context_data( *args, **kwargs)
    users =  User.objects.all().order_by('-date_joined')
    validshares =  SharesPayment.objects.filter(is_id=True,is_valid=True).order_by('-date_added')
    staffs =  User.objects.filter(is_staff = True).order_by('-date_joined')
    admins =  User.objects.filter(is_superuser = True).order_by('-date_joined')
    mails = Mail.objects.filter(seen= False)
    context.update({'users':users,'validshares':validshares, 'mails':mails,'staffs':staffs, 'admins':admins})
    return context
  def test_func(self):
    if self.request.user.is_superuser or self.request.user.is_staff:
      return True
    return False

class Emails(UserPassesTestMixin,ListView ):
    model = Mail
    template_name = 'dashboard/inbox.html'
    def get_context_data(self, *args,**kwargs: any):
        context = super(Emails,self).get_context_data(*args,**kwargs)
        mails = Mail.objects.filter(seen = False).order_by('-date_added')
        context.update({'mails':mails})
        return context    
    def post(self,request,*args, **kwargs):
        if request.method =='POST':
            try:
                id = request.POST['mail']
                mail = Mail.objects.get(id = int(id))
                mail.seen = True
                mail.save()
                return redirect('mails')
            except Exception:
                return redirect('mails')
                

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False

class MakeMail(UserPassesTestMixin,TemplateView ):
    model = Mail
    template_name = 'dashboard/compose.html'
    def post(self,request,*args, **kwargs):
        if request.method =='POST':
            try:
                email = request.POST['email']
                subject =request.POST['subject']
                body =request.POST['message']
                msg = EmailMessage()
                msg['To'] = email  
                msg['subject'] = subject
                msg['From'] =f'no-reply<{mail_username}>'
                msg.set_content(body)
                try:
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(mail_username, mail_password)
                        smtp.send_message(msg)
                        messages.success(request,'Mail Sent Succesfully!')
                        return redirect('makemail')
                except Exception as error:
                    messages.info(request, f'Error : {error}')
                    return redirect('makemail')

            except Exception as err:
                print('there is errrrro: ',err)
                return redirect('mails')
    def test_func(self):
        if self.request.user.is_superuser  or self.request.user.is_staff:
            return True
        return False

class SharePayment(UserPassesTestMixin,ListView ):
    model = SharesPayment
    template_name = 'dashboard/sharepayment.html'

    def get_context_data(self, *args,**kwargs: any):
        context = super(SharePayment,self).get_context_data(*args,**kwargs)
        mails = Mail.objects.filter(seen= False)
        validshares = SharesPayment.objects.filter(is_id = True, is_valid=True).order_by('-date_added')
        invalidshares = SharesPayment.objects.filter(is_id = True, is_valid=False).order_by('-date_added')
        context.update({'validshares':validshares, 'invalidshares':invalidshares,'mails':mails})
        return context 

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class FarmPayment(UserPassesTestMixin,ListView ):
    model = FarmsPayment
    template_name = 'dashboard/farmpayment.html'

    def get_context_data(self, *args,**kwargs: any):
        context = super(FarmPayment,self).get_context_data(*args,**kwargs)
        validpays = FarmsPayment.objects.filter(is_id = True, is_valid=True).order_by('-date_added')
        invalidpays = FarmsPayment.objects.filter(is_id = True, is_valid=False).order_by('-date_added')
        mails = Mail.objects.filter(seen= False)

        context.update({'validpays':validpays, 'invalidpays':invalidpays,'mails':mails})
        return context 
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class AllUsers(UserPassesTestMixin,ListView ):
    model = User
    template_name = 'dashboard/users.html'
    paginate_by = 12
    context_object_name = 'users'
    ordering = ['-date_joined']
    def get_context_data(self, *args,**kwargs: any):
        context = super(AllUsers,self).get_context_data(*args,**kwargs)
        mails = Mail.objects.filter(seen= False)
        context.update({ 'mails':mails})
        return context 
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False

class Workers(UserPassesTestMixin,ListView):
    model = AvailableWorker
    template_name = 'dashboard/workers.html'
    context_object_name = 'workers'

    paginate_by = 10
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False

class AddStaff(UserPassesTestMixin,UpdateView):
    model = User
    success_url = '/dashboard/'
    fields = ['username','is_staff']
    template_name = 'dashboard/staff.html'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
    

