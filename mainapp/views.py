from asyncio.windows_events import NULL
from inspect import _empty
from queue import Empty
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    TemplateView,
    ListView,
    DetailView,

)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import GreenlandFarms, Profile,Crop,Advert,AvailableJob,AvailableWorker,Land,GreenlandFarms,FarmImpliments, Shares
from users.models import LandRequest
from email.message import EmailMessage
import smtplib
from django.conf import settings

mail_username = settings.EMAIL_HOST_USER
mail_password = settings.EMAIL_HOST_PASSWORD
# Home view
def home(request):
    crops = Crop.objects.all().order_by('-date_added')
    adverts = Advert.objects.all().order_by('-date_added')
    jobs = AvailableJob.objects.all().order_by('-date_added')
    workers = AvailableWorker.objects.filter(approved = True)
    lands = Land.objects.all().order_by('-date_added')
    farms = GreenlandFarms.objects.all().order_by('-date_added')
    impliments = FarmImpliments.objects.all().order_by('-date_added')
    context = {
        'crops':crops,
        'adverts':adverts,
        'jobs':jobs,
        'workers':workers,
        'lands':lands,
        'farms':farms,
        'impliments':impliments,

    }
   
    return render(request, 'mainapp/home.html', context)

# registration page view

def usersRegister(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username','email')
            messages.success(request, f' Account for {username} was created!  Login Now')
            msg = EmailMessage()
            msg['To'] = request.POST['email']  
            body = f"Welcome to Greenlands farms you register as {request.POST['username']}"
            msg['subject'] = 'Welcome To greenLands NG'
            msg['From'] =f'no-reply<{mail_username}>'
            msg.set_content(body)
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(mail_username, mail_password)
                    smtp.send_message(msg)
            except Exception as error:
                messages.info(request, f'Error : {error}')
                
            return redirect('login')

    form = UserRegistrationForm()
    return render(request, 'dashboard/register.html', {"form":form,"title":"User Registration"})


def shares(request):
    shares = Shares.objects.all().order_by('-date_added')
    context = {
        'shares':shares,
    }
    return render(request,'mainapp/shares.html',context)


# create views
class CropCreateView(UserPassesTestMixin,CreateView):
    model = Crop
    fields = '__all__'
    template_name = 'mainapp/create.html'

    success_url = '/'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
        
class AdvertCreateView(UserPassesTestMixin,CreateView):
    model = Advert
    success_url = '/'
    fields = '__all__'

    template_name = 'mainapp/create.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class GreenlandFarmsCreateView(UserPassesTestMixin,CreateView):
    model = GreenlandFarms
    success_url = '/'
    fields = '__all__'

    template_name = 'mainapp/create.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class FarmImplimentsCreateView(UserPassesTestMixin,CreateView):
    model = FarmImpliments
    success_url = '/'
    fields = '__all__'
    template_name = 'mainapp/create.html'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
        
class LandCreateView(UserPassesTestMixin,CreateView):
    model = Land
    template_name = 'mainapp/create.html'
    success_url = '/'
    fields = '__all__'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
class AvailableWorkerCreateView(UserPassesTestMixin,CreateView):
    model = AvailableWorker
    success_url = '/'
    fields = '__all__'
    template_name = 'mainapp/create.html'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class AvailableJobCreateView(LoginRequiredMixin,CreateView):
    model = AvailableJob
    fields = ['type_of_work', 'local_govt','state','country','description','number_of_workers','cost']
    template_name = 'mainapp/create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
# Update  views
class CropUpdateView(UserPassesTestMixin,UpdateView):
    model = Crop
    fields = '__all__'
    template_name = 'mainapp/update.html'

    success_url = '/'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class AdvertUpdateView(UserPassesTestMixin,UpdateView):
    model = Advert
    success_url = '/'
    fields = '__all__'

    template_name = 'mainapp/update.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class GreenlandFarmsUpdateView(UserPassesTestMixin,UpdateView):
    model = GreenlandFarms
    success_url = '/'
    fields = '__all__'
    template_name = 'mainapp/update.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class FarmImplimentsUpdateView(UserPassesTestMixin,UpdateView):
    model = FarmImpliments
    success_url = '/'
    fields = '__all__'

    template_name = 'mainapp/update.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class LandUpdateView(UserPassesTestMixin,UpdateView):
    model = Land
    fields = '__all__'
    template_name = 'mainapp/update.html'
    success_url = '/'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class AvailableJobUpdateView(UserPassesTestMixin,UpdateView):
    model = AvailableJob
    success_url = '/'
    fields = '__all__'
    template_name = 'mainapp/Update.html'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class AvailableWorkerUpdateView(UserPassesTestMixin,UpdateView):
    model = AvailableWorker
    success_url = '/'
    fields = '__all__'
    template_name = 'mainapp/Update.html'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

# Home Delete  views
class CropDeleteView(UserPassesTestMixin,DeleteView):
    model = Crop
    template_name = 'mainapp/delete.html'

    success_url = '/'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class AdvertDeleteView(UserPassesTestMixin,DeleteView):
    model = Advert
    success_url = '/'
    template_name = 'mainapp/delete.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class GreenlandFarmsDeleteView(UserPassesTestMixin,DeleteView):
    model = GreenlandFarms
    success_url = '/'
    template_name = 'mainapp/delete.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class FarmImplimentsDeleteView(UserPassesTestMixin,DeleteView):
    model = FarmImpliments
    success_url = '/'
    template_name = 'mainapp/delete.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class LandDeleteView(UserPassesTestMixin,DeleteView):
    model = Land
    template_name = 'mainapp/delete.html'
    success_url = '/'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class AvailableJobDeleteView(UserPassesTestMixin,DeleteView):
    model = AvailableJob
    success_url = '/'
    template_name = 'mainapp/delete.html'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class AvailableWorkerDeleteView(UserPassesTestMixin,DeleteView):
    model = AvailableWorker
    success_url = '/'
    template_name = 'mainapp/delete.html'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

#Home  list views
class AdvertListView(ListView):
    model = Advert
    paginate_by = 3
    template_name = 'mainapp/itemslist.html'
    def get_context_data(self, *args, **kwargs):
        context =super(AdvertListView,self).get_context_data( *args, **kwargs)
        advert=  Advert.objects.all().order_by('-date_added')

        context.update({'advert':advert})
        return context

class GreenlandFarmsListView(ListView):
    model = GreenlandFarms
    paginate_by = 3
    template_name = 'mainapp/farms_list.html'
    def get_context_data(self, *args, **kwargs):
        context =super(GreenlandFarmsListView,self).get_context_data( *args, **kwargs)
        first_quarters=  GreenlandFarms.objects.filter(first_quarter=True).order_by('-date_added')
        second_quarters=  GreenlandFarms.objects.filter(second_quarter= True).order_by('-date_added')

        context.update({'first_quarters':first_quarters,'second_quarters':second_quarters})
        return context

class LandListView(ListView):
    model = Land
    paginate_by = 5
    # context_object_name = 'lands'
    template_name = 'mainapp/land_list.html'
    def get_context_data(self, *args, **kwargs):
        context =super(LandListView,self).get_context_data( *args, **kwargs)
        lands=  Land.objects.all().order_by('-date_added')

        context.update({'lands':lands})
        return context


class FarmImplimentssListView(ListView):
    model = FarmImpliments
    context_object_name = 'tools'
    ordering = ['-date_added']
    paginate_by = 5    
    template_name = 'mainapp/farmimpliments_list.html'
    def get_context_data(self, *args, **kwargs):
        context =super(FarmImplimentssListView,self).get_context_data( *args, **kwargs)
        tool=  FarmImpliments.objects.all().order_by('-date_added')

        context.update({'tool':tool})
        return context

class WorkerListView(ListView):
    model = AvailableWorker
    paginate_by = 10
    template_name = 'users/workers.html'
    context_object_name = 'workers'

class JobListView(ListView):
    model = AvailableJob
    context_object_name = 'jobs'
    template_name = 'users/jobs.html'
    def get_context_data(self,*args, **kwargs: any):
        context = super(JobListView,self).get_context_data(*args,**kwargs)
        alljobs = AvailableJob.objects.all().order_by('-date_added')
        context.update({'alljobs':alljobs})
        return  context
# detail Views
class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'users/advert_detail.html'

class GreenlandFarmsDetailView(DetailView):
    model = GreenlandFarms
    template_name = 'users/farm_detail.html'


class LandDetailView(DetailView):
    model = Land
    template_name = 'mainapp/land_details.html'
 
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        if request.method =='POST':
            land = Land.objects.get(id = pk)
            full_name = request.POST['full_name']
            phone = request.POST['phone']
            email = request.POST['email']
            message = request.POST['message']
            if message:
                if phone: 
                    if full_name:
                        obj = LandRequest(land = land,customer_name = full_name,customer_phone=phone,
                        customer_message =message, customer_mail = email
                        )
                        obj.save()
                        messages.success(request,'Your request was sent successfully!')
                        return redirect('home')
                    else:
                        messages.info(request,'Please fill the form completely')
                        return redirect('landdetail', pk)
                else:
                    messages.info(request,'Please fill the form completely')
                    return redirect('landdetail', pk)
            else:
                messages.info(request,'Please fill the form completely')
                return redirect('landdetail', pk)

        

class FarmImplimentssDetailView(DetailView):
    model = FarmImpliments
    template_name = 'mainapp/tools_detail.html'
    def get_context_data(self, *args, **kwargs):
        context =super(FarmImplimentssDetailView,self).get_context_data( *args, **kwargs)
        tools=  FarmImpliments.objects.all().order_by('-date_added')

        context.update({'tools':tools})
        return context

class AvailableWorkerDetailView(DetailView):
    model = AvailableWorker
    template_name = 'mainapp/detail.html'

class AvailableJobDetailView(DetailView):
    model = AvailableJob
    template_name = 'users/jobs_detail.html'
    def get_context_data(self,*args, **kwargs: any):
        context = super(AvailableJobDetailView,self).get_context_data(*args,**kwargs)
        alljobs = AvailableJob.objects.all().order_by('-date_added')
        context.update({'alljobs':alljobs})
        return  context
   
def about(request):
    return render(request,'users/about.html')
