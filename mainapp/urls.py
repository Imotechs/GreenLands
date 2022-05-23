
from django.urls import path
from .views import(
     home,
    usersRegister,
    shares,
    about,
    #home create Views
    CropCreateView,
    LandCreateView,
    GreenlandFarmsCreateView,
    AdvertCreateView,
    AvailableJobCreateView,
    AvailableWorkerCreateView,
    FarmImplimentsCreateView,
    #home update views
    CropUpdateView,
    LandUpdateView,
    GreenlandFarmsUpdateView,
    AdvertUpdateView,
    AvailableJobUpdateView,
    FarmImplimentsUpdateView,
    AvailableWorkerUpdateView,

    #home delete views
    CropDeleteView,
    LandDeleteView,
    GreenlandFarmsDeleteView,
    AdvertDeleteView,
    AvailableJobDeleteView,
    FarmImplimentsDeleteView,
    AvailableWorkerDeleteView,
    #home detail views
    AdvertDetailView,
    GreenlandFarmsDetailView,
    LandDetailView,
    AvailableWorkerDetailView,
    FarmImplimentssDetailView,
    AvailableJobDetailView,
    #Home List Views
    AdvertListView,
    GreenlandFarmsListView,
    LandListView,
    FarmImplimentssListView,
    WorkerListView,
    JobListView,

)
import users.views as user_views


urlpatterns = [
    path('', home, name = 'home' ),
    path('users/registrations/', usersRegister, name = 'register'),
    path('our/shares/',shares, name = 'shares'),
    path('accounts/profile/', user_views.profile, name = 'profile'),
    path('our/terms/conditions/', user_views.terms, name = 'terms'),
    path('help/me/', user_views.help, name = 'help'),
    path('contact/us/', user_views.contact, name = 'contact'),
    path('about/us/', about, name = 'about'),
    #create home urls
    path('add/crop/', CropCreateView.as_view(), name = 'addcrop'),
    path('add/lands/', LandCreateView.as_view(), name = 'addland'),
    path('add/GreenLandFarms/', GreenlandFarmsCreateView.as_view(), name = 'addfarm'),
    path('add/advert/', AdvertCreateView.as_view(), name = 'addadvert'),
    path('add/jobs/', AvailableJobCreateView.as_view(), name = 'addjob'),
    path('add/worker/', AvailableWorkerCreateView.as_view(), name = 'addworker'),
    path('add/tool/', FarmImplimentsCreateView.as_view(), name = 'addtool'),
    #update home urls
    path('update/<int:pk>/crop/', CropUpdateView.as_view(), name = 'updatecrop'),
    path('update/<int:pk>/lands/', LandUpdateView.as_view(), name = 'updateland'),
    path('update/<int:pk>/GreenLandFarms/', GreenlandFarmsUpdateView.as_view(), name = 'updatefarm'),
    path('update/<int:pk>/advert/', AdvertUpdateView.as_view(), name = 'updateadvert'),
    path('update/<int:pk>/jobs/', AvailableJobUpdateView.as_view(), name = 'updatejob'),
    path('update/<int:pk>/worker/', AvailableWorkerUpdateView.as_view(), name = 'updateworker'),
    path('update/<int:pk>/tool/', FarmImplimentsUpdateView.as_view(), name = 'updatetool'),
    #delet home urls
    path('delete/<int:pk>/crop/', CropDeleteView.as_view(), name = 'deletecrop'),
    path('delete/<int:pk>/lands/', LandDeleteView.as_view(), name = 'deleteland'),
    path('delete/<int:pk>/GreenLandFarms/', GreenlandFarmsDeleteView.as_view(), name = 'deletefarm'),
    path('delete/<int:pk>/advert/', AdvertDeleteView.as_view(), name = 'deleteadvert'),
    path('delete/<int:pk>/jobs/', AvailableJobDeleteView.as_view(), name = 'deletejob'),
    path('delete/<int:pk>/worker/', AvailableWorkerDeleteView.as_view(), name = 'deleteworker'),
    path('delete/<int:pk>/tool/', FarmImplimentsDeleteView.as_view(), name = 'deletetool'),
    #home items detail urls
    path('advert/<int:pk>/detail/', AdvertDetailView.as_view(), name = 'advertdetail'),
    path('GreenLandFarms/<int:pk>/detail/', GreenlandFarmsDetailView.as_view(), name = 'farmdetail'),
    path('land/<int:pk>/detail/', LandDetailView.as_view(), name = 'landdetail'),
    path('worker/<int:pk>/detail/', AvailableWorkerDetailView.as_view(), name = 'workerdetail'),
    path('job/<int:pk>/detail/', AvailableJobDetailView.as_view(), name = 'jobdetail'),
    path('farm/<int:pk>/tool/detail/', FarmImplimentssDetailView.as_view(), name = 'tooldetail'),
    #home list views
    path('advert/list/',AdvertListView.as_view(), name = 'advertlist'),
    path('GreenLandFarms/list/',GreenlandFarmsListView.as_view(), name = 'farmlist'),
    path('land/list/',LandListView.as_view(), name = 'landlist'),
    path('farm/tools/list/',FarmImplimentssListView.as_view(), name = 'toollist'),
    path('workers/list/',WorkerListView.as_view(), name = 'workerlist'),
    path('jobs/list/',JobListView.as_view(), name = 'joblist'),
    #payment
    path('checkout/<int:pk>/',user_views.payment_checkout, name = 'checkout'),
    path('make/payment/<int:pk>/',user_views.FlutterPayView.as_view(), name = 'payment'),
    path('payment/success/', user_views.PaymentSuccess.as_view(), name = 'paymentsuccess'),
    path('shares/<int:pk>/', user_views.sharesform, name = 'sharesform'),
    path('share/make/payment/<int:pk>/',user_views.FlutterSharePayView.as_view(), name = 'sharepayment'),
    path('share/payment/success/', user_views.SharePaymentSuccess.as_view(), name = 'sharepaymentsuccess'),


]
