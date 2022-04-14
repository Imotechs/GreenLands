from django.contrib.auth.models import User
from django import forms
from mainapp.models import AvailableJob, Profile,AvailableWorker
from .models import Mail,UserAdress

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name'] 
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args,**kwargs)
        for fieldname in ['username','email','first_name', 'last_name']:
            self.fields[fieldname].help_text = None

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo','phone']
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args,**kwargs)
        for fieldname in ['photo','phone']:
            self.fields[fieldname].help_text = None

class WorkerForm(forms.ModelForm):
    class Meta:
        model = AvailableWorker
        fields = ['phone','id_card','id_number','description']
    def __init__(self, *args, **kwargs):
        super(WorkerForm, self).__init__(*args,**kwargs)
        for fieldname in ['phone','id_card','id_number']:
            self.fields[fieldname].help_text = None


class JobForm(forms.ModelForm):
    class Meta:
        model = AvailableJob
        fields = ['type_of_work','local_govt','state','country','photo','description','number_of_workers','cost']
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args,**kwargs)
        for fieldname in ['type_of_work','local_govt','state','country','photo','description','number_of_workers','cost']:
            self.fields[fieldname].help_text = None
  


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['your_name','email_address','phone_number','how_can_we_help_you']
    def __init__(self, *args, **kwargs):
        super(MailForm, self).__init__(*args,**kwargs)
        for fieldname in ['your_name','email_address','phone_number','how_can_we_help_you']:
            self.fields[fieldname].help_text = None


class UserAdressForm(forms.ModelForm):
    class Meta:
        model = UserAdress
        fields = ['detail_address']
    