from django.shortcuts import render, redirect

from mainapp.models import AvailableJob, AvailableWorker, FarmImpliments, Profile, GreenlandFarms, Shares
from users.models import UserAdress,FarmsPayment, SharesPayment
from .forms import JobForm, MailForm, UserUpdateForm,ProfileForm,WorkerForm,UserAdressForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import functions
from django.views.generic import TemplateView, View, ListView
# Create your views here.


#  users profiles
@login_required
def profile(request):
    if request.method == 'POST':
            try:
                U_form = UserUpdateForm(request.POST, instance= request.user)
                P_form = ProfileForm(request.POST, 
                                        request.FILES, 
                                        instance = request.user)              
                if U_form.is_valid() and P_form.is_valid():
                    user = Profile.objects.filter(user = request.user)
                    U_form.save()
                    if not user:
                        try:
                            obj =  Profile(user = request.user,photo = request.FILES['photo'],phone = request.POST['phone'])
                            obj.save()
                            messages.success(request, f'Your profile  was added!')
                            return redirect ('profile')
                        except Exception:
                            pass
                    try:   
                        P_form = ProfileForm(request.POST, 
                                           request.FILES, 
                                            instance = request.user.profile)
                        P_form.save()
                        messages.success(request, f'Your profile was updated!')
                        return redirect ('profile')
                    except Exception as er:
                        print('we have an error :', er)
                        pass

                elif P_form.is_valid():
                    user = Profile.objects.filter(user = request.user)
                    if not user:
                        try:
                            obj =  Profile(user = request.user,photo = request.FILES['photo'],phone = request.POST['phone'])
                            obj.save()
                            messages.success(request, f'{request.user.username} profile photo was added!')
                            return redirect ('profile')
                        except Exception:
                            pass
                    try:   
                        P_form = ProfileForm(request.POST, 
                                            request.FILES['photo'], 
                                            instance = request.user.profile)
                        P_form.save()
                        messages.success(request, f'Your profile was updated!')
                        return redirect ('profile')
                    except Exception:
                        pass
                else:
                    pass


                W_form = WorkerForm(request.POST,request.FILES, instance= request.user)
                if W_form.is_valid():
                    try:
                        current_worker = AvailableWorker.objects.filter(user = request.user)
                        if current_worker:
                            messages.info(request,'you are already a worker')
                            return redirect('profile')
                        obj = AvailableWorker(user = request.user,phone = request.POST['phone'],
                        id_card = request.FILES['id_card'],
                        id_number = request.POST['id_number'],
                        local_govt = request.POST['local_govt'],
                        state = request.POST['state'],
                        country = request.POST['country'],
                        )
                        obj.save()
                        messages.success(request,'Your Application was succesful!, waite for Approval')
                        return redirect('profile')
                    except Exception as err:
                        print('we have an error:',err)
                        pass

                J_form = JobForm(request.POST, request.FILES, instance = request.user)
                if J_form.is_valid():
                    try:
                        obj = AvailableJob(

                            user = request.user,
                            photo = request.FILES['photo'],
                            type_of_work = request.POST['type_of_work'],
                            local_govt = request.POST['local_govt'],
                            state = request.POST['state'],
                            country = request.POST['country'],
                            number_of_workers = request.POST['number_of_workers'],
                            description  =request.POST['description'],
                            cost =request.POST['cost'],
                            available = True,
                            approved= False,
                        )

                        obj.save()
                        messages.success(request, ' Thank you, Your Job was sent')
                        return redirect('profile')
                    except Exception as ero:
                        print('this error:', ero)
                        messages.info(request, 'Your Job Was not sent, pls Try again')
                        pass


                
                try:        
                    adress = request.POST['detail_address']
                    if adress:
                        user = UserAdress.objects.filter(user = request.user)
                        if not user:
                            obj = UserAdress(detail_address = adress,user=request.user)
                            obj.save()
                            messages.success(request,'You Added your Address')
                            return redirect('profile')
                        A_form = UserAdressForm(request.POST,instance=request.user.useradress)
                        A_form.save()
                        messages.success(request,'Your Adress was Successfully Updated')
                        return redirect('profile')
                    else:
                        messages.error(request, 'FormErr, Try Again')
                        pass
                except Exception:
                    pass

            except AttributeError as erro:
                print('Error:'+ str(erro))
                return redirect ('login')


    try:
        A_form = UserAdressForm(instance = request.user.useradress)
        is_worker = AvailableWorker.objects.filter(user = request.user)
        J_form = JobForm()
        W_form = WorkerForm()
        U_form = UserUpdateForm(instance= request.user)
        P_form = ProfileForm(instance = request.user.profile)   
        user = User.objects.filter(id = request.user.id)
        context = {
            'user':user[0],
            'U_form':U_form,
            'P_form':P_form,
            'W_form':W_form,
            'J_form':J_form,
            'A_form':A_form,
            'is_worker':is_worker
        }
        return render(request, 'mainapp/profile.html',context)

    except Exception:
        J_form = JobForm()
        A_form = UserAdressForm()
        W_form = WorkerForm()
        is_worker = AvailableWorker.objects.filter(user = request.user)

        U_form = UserUpdateForm(instance= request.user)
        P_form = ProfileForm(instance = request.user)   
        user = User.objects.filter(id = request.user.id)
        context = {
            'user':user[0],
            'U_form':U_form,
            'P_form':P_form,
            'W_form':W_form,
            'J_form':J_form,
            'A_form':A_form,
            'is_worker':is_worker


        }
        return render(request, 'mainapp/profile.html',context)


def terms(request):
     return render(request,'mainapp/terms.html')

def help(request):
     return render(request,'mainapp/help.html')

def contact(request):
    if request.method =='POST':
        form = MailForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your messages was Sent!')
            form.save()
            return redirect('/')
            
    form = MailForm()
    context = {
        'form':form,
    }
    return render(request,'mainapp/contact.html',context)


#payment Gateway


class FlutterPayView(TemplateView):
    template_name = 'users/flutter.html'
    def get_context_data(self, **kwargs: any):
        job_id =self.kwargs['pk']
        user = self.request.user
        payment = FarmsPayment.objects.filter(id = job_id)

        context = super(FlutterPayView,self).get_context_data(**kwargs)
        context.update({
              'user':user,
            'payment':payment[0],
            'FLUTTER_KEYS':settings.FLUTTER_KEYS
        })
        return context
        
@login_required
def payment_checkout(request,pk):
    current_payment = FarmsPayment.objects.filter(user = request.user,
                            farm =GreenlandFarms.objects.get(id = pk), is_id = True, is_valid = False)
    if request.method =='POST':
            if not current_payment:
                farm = GreenlandFarms.objects.get(id = pk)
                txn_id = functions.get_payment_id('Frm')
                obj = FarmsPayment(user = request.user,transaction_id = txn_id,
                            farm =farm, is_id = True, cost =farm.cost )
                obj.save()
                messages.info(request, f'Make your Payment!')
                payment = FarmsPayment.objects.filter(user = request.user, transaction_id = txn_id)
                payment_pk = payment[0].id
                return redirect('payment',int(payment_pk))

            else: 
                messages.info(request,f'You initiated this payment before pls make your payment')
                return redirect('payment',int(current_payment[0].id))

    farm = GreenlandFarms.objects.get(id = pk)
    context = {
        'farm':farm,
    }
    return render(request,'users/checkout.html',context)

class PaymentSuccess(View):
  def post(self,request,*args, **kwargs):#here and below
       

        return render(request,'mainapp/payment_succes.html') 
        
  def get(self,request,*args, **kwargs):
    if request.method == 'GET':
      obj = FarmsPayment.objects.get(user =request.user,
                                  transaction_id =request.GET['tx_ref'],
              is_id = True)
      if obj:
        obj.is_valid =True
        obj.save()
        messages.success(request,'your payment was succesfull')
        return render(request,'users/payment_succes.html')
    
@login_required
def sharesform(request,pk):
    share_id = pk
    chosenshare = Shares.objects.filter(id =pk)
    share = SharesPayment.objects.filter(user = request.user,
            shares = Shares.objects.get(id = share_id))
    if share:
        if share[0].is_id and share[0].is_valid:
            messages.info(request, 'You have Paid for This Share!')
            return redirect('profile')
        if share[0].is_id and not share[0].is_valid:
            messages.info(request,'You Submmited Application for this Shares!')
            messages.info(request,'You Can make your Payment Now')
            return redirect('sharepayment', int(share[0].id))

    if request.method =='POST':
        cost = int(request.POST['amount']),
        print(cost[0])
        obj = SharesPayment(
        user = request.user,
        full_name = request.POST['full_name'],
        phone = request.POST['phone'],
        status = request.POST['status'],
        work_status = request.POST['work_status'],
        address = request.POST['address'],
        email = request.POST['email'],
        id_number = request.POST['id_number'],
        id_type = request.POST['id_type'],
        country = request.POST['Country'],
        DOBd = request.POST['dobd'],
        DOBm = request.POST['dobm'],
        DOBy = request.POST['doby'],
        gender = request.POST['gender'],
        payment_method = request.POST['payment_method'],
        acc_number = request.POST['acc_number'],
        bank = request.POST['bank'],
        acc_type = request.POST['acc_type'],
        cost = request.POST['amount'],
        shares = Shares.objects.get(id =pk),
        transaction_id = functions.get_payment_id('shrs'),
        is_id = True,
        )
        if not cost[0] < chosenshare[0].min_cost:
            obj.save()
            item = SharesPayment.objects.get(transaction_id = obj.transaction_id)
            return redirect('sharepayment',int(item.id))
        messages.info(request, 'Sorry You Tried To invest a Lower Amount')
        messages.info(request, 'Try Agin with amount greater or equal to Min Value specified')
        return redirect('shares')

    
    choice = Shares.objects.get(id =pk)
    context = {
        'shares':choice,
    }
    return render(request, 'users/sharesform.html',context)


class FlutterSharePayView(TemplateView):
    template_name = 'users/share_flutter.html'
    def get_context_data(self, **kwargs: any):
        job_id =self.kwargs['pk']
        user = self.request.user
        payment = SharesPayment.objects.filter(id = job_id)

        context = super(FlutterSharePayView,self).get_context_data(**kwargs)
        context.update({
              'user':user,
            'payment':payment[0],
            'FLUTTER_KEYS':settings.FLUTTER_KEYS
        })
        return context
class SharePaymentSuccess(View):
  def get(self,request,*args, **kwargs):
    if request.method == 'GET':
      obj = SharesPayment.objects.get(user =request.user,
                                  transaction_id =request.GET['tx_ref'],
              is_id = True)
      if obj:
        obj.is_valid =True
        obj.save()
        messages.success(request,'your payment was succesfull')
        return render(request,'users/payment_succes.html')