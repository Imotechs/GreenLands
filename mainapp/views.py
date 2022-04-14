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
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Profile,Crop,Advert,AvailableJob,AvailableWorker,Land,Trending,Farm_Tool
# Home view
def home(request):
    crops = Crop.objects.all().order_by('-date_added')
    adverts = Advert.objects.all().order_by('-date_added')
    jobs = AvailableJob.objects.all().order_by('-date_added')
    workers = AvailableWorker.objects.filter(approved = True)
    lands = Land.objects.all().order_by('-date_added')
    trendings = Trending.objects.all().order_by('-date_added')
    farm_tools = Farm_Tool.objects.all().order_by('-date_added')
    context = {
        'crops':crops,
        'adverts':adverts,
        'jobs':jobs,
        'workers':workers,
        'lands':lands,
        'trendings':trendings,
        'farm_tools':farm_tools,

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
            return redirect('login')

    form = UserRegistrationForm()
    return render(request, 'mainapp/register.html', {"form":form,"title":"User Registration"})


def shares(request):
    return render(request,'mainapp/shares.html')


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

class TrendingCreateView(UserPassesTestMixin,CreateView):
    model = Trending
    success_url = '/'
    fields = '__all__'

    template_name = 'mainapp/create.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class FarmToolCreateView(UserPassesTestMixin,CreateView):
    model = Farm_Tool
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

class AvailableJobCreateView(UserPassesTestMixin,CreateView):
    model = AvailableJob
    success_url = '/'
    fields = '__all__'

    template_name = 'mainapp/create.html'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
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

class TrendingUpdateView(UserPassesTestMixin,UpdateView):
    model = Trending
    success_url = '/'
    fields = '__all__'
    template_name = 'mainapp/update.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class FarmToolUpdateView(UserPassesTestMixin,UpdateView):
    model = Farm_Tool
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

class TrendingDeleteView(UserPassesTestMixin,DeleteView):
    model = Trending
    success_url = '/'
    template_name = 'mainapp/delete.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class FarmToolDeleteView(UserPassesTestMixin,DeleteView):
    model = Farm_Tool
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

class TrendingListView(ListView):
    model = Trending
    paginate_by = 3
    template_name = 'mainapp/trending.html'
    def get_context_data(self, *args, **kwargs):
        context =super(TrendingListView,self).get_context_data( *args, **kwargs)
        first_quarters=  Trending.objects.filter(first_quarter=True).order_by('-date_added')
        second_quarters=  Trending.objects.filter(second_quarter= True).order_by('-date_added')

        context.update({'first_quarters':first_quarters,'second_quarters':second_quarters})
        return context

class LandListView(ListView):
    model = Land
    paginate_by = 3
    template_name = 'mainapp/itemslist.html'
    def get_context_data(self, *args, **kwargs):
        context =super(LandListView,self).get_context_data( *args, **kwargs)
        lands=  Land.objects.all().order_by('-date_added')

        context.update({'lands':lands})
        return context


class FarmToolsListView(ListView):
    model = Farm_Tool
    context_object_name = 'tools'
    ordering = ['-date_added']
    paginate_by = 2    
    template_name = 'mainapp/farmtools.html'
    def get_context_data(self, *args, **kwargs):
        context =super(FarmToolsListView,self).get_context_data( *args, **kwargs)
        tool=  Farm_Tool.objects.all().order_by('-date_added')

        context.update({'tool':tool})
        return context

class WorkerListView(ListView):
    model = AvailableWorker
    paginate_by = 10
    template_name = 'mainapp/itemslist.html'

class JobListView(ListView):
    model = AvailableJob
    paginate_by = 10
    template_name = 'mainapp/itemslist.html'
# detail Views
class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'mainapp/detail.html'

class TrendingDetailView(DetailView):
    model = Trending
    template_name = 'mainapp/detail.html'


class LandDetailView(DetailView):
    model = Land
    template_name = 'mainapp/detail.html'
   

class FarmToolsDetailView(DetailView):
    model = Farm_Tool
    template_name = 'mainapp/tools_detail.html'
    def get_context_data(self, *args, **kwargs):
        context =super(FarmToolsDetailView,self).get_context_data( *args, **kwargs)
        tools=  Farm_Tool.objects.all().order_by('-date_added')

        context.update({'tools':tools})
        return context

class AvailableWorkerDetailView(DetailView):
    model = AvailableWorker
    template_name = 'mainapp/detail.html'

class AvailableJobDetailView(DetailView):
    model = AvailableJob
    template_name = 'mainapp/detail.html' 
   

