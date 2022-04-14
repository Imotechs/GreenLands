from multiprocessing import context
from django.shortcuts import render, redirect

from mainapp.models import AvailableJob, AvailableWorker, Profile
from users.models import UserAdress
from .forms import JobForm, MailForm, UserUpdateForm,ProfileForm,WorkerForm,UserAdressForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
                        obj = AvailableWorker(user = request.user,phone = request.POST['phone'],id_card = request.FILES['id_card'],id_number = request.POST['id_number'])
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


        }
        return render(request, 'mainapp/profile.html',context)

    except Exception:
        J_form = JobForm()
        A_form = UserAdressForm()
        W_form = WorkerForm()
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