
from django.urls import path
from .views import(
     home,
    usersRegister,
    shares,
    #home create Views
    CropCreateView,
    LandCreateView,
    TrendingCreateView,
    AdvertCreateView,
    AvailableJobCreateView,
    AvailableWorkerCreateView,
    FarmToolCreateView,
    #home update views
    CropUpdateView,
    LandUpdateView,
    TrendingUpdateView,
    AdvertUpdateView,
    AvailableJobUpdateView,
    FarmToolUpdateView,
    AvailableWorkerUpdateView,

    #home delete views
    CropDeleteView,
    LandDeleteView,
    TrendingDeleteView,
    AdvertDeleteView,
    AvailableJobDeleteView,
    FarmToolDeleteView,
    AvailableWorkerDeleteView,
    #home detail views
    AdvertDetailView,
    TrendingDetailView,
    LandDetailView,
    AvailableWorkerDetailView,
    FarmToolsDetailView,
    AvailableJobDetailView,
    #Home List Views
    AdvertListView,
    TrendingListView,
    LandListView,
    FarmToolsListView,
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
    #create home urls
    path('add/crop/', CropCreateView.as_view(), name = 'addcrop'),
    path('add/lands/', LandCreateView.as_view(), name = 'addland'),
    path('add/trending/', TrendingCreateView.as_view(), name = 'addtrending'),
    path('add/advert/', AdvertCreateView.as_view(), name = 'addadvert'),
    path('add/jobs/', AvailableJobCreateView.as_view, name = 'addjob'),
    path('add/worker/', AvailableWorkerCreateView.as_view(), name = 'addworker'),
    path('add/tool/', FarmToolCreateView.as_view, name = 'addtool'),
    #update home urls
    path('update/<int:pk>/crop/', CropUpdateView.as_view(), name = 'updatecrop'),
    path('update/<int:pk>/lands/', LandUpdateView.as_view(), name = 'updateland'),
    path('update/<int:pk>/trending/', TrendingUpdateView.as_view(), name = 'updatetrending'),
    path('update/<int:pk>/advert/', AdvertUpdateView.as_view(), name = 'updateadvert'),
    path('update/<int:pk>/jobs/', AvailableJobUpdateView.as_view, name = 'updatejob'),
    path('update/<int:pk>/worker/', AvailableWorkerUpdateView.as_view, name = 'updateworker'),
    path('update/<int:pk>/tool/', FarmToolUpdateView.as_view, name = 'updatetool'),
    #delet home urls
    path('delete/<int:pk>/crop/', CropDeleteView.as_view(), name = 'deletecrop'),
    path('delete/<int:pk>/lands/', LandDeleteView.as_view(), name = 'deleteland'),
    path('delete/<int:pk>/trending/', TrendingDeleteView.as_view(), name = 'deletetrending'),
    path('delete/<int:pk>/advert/', AdvertDeleteView.as_view(), name = 'deleteadvert'),
    path('delete/<int:pk>/jobs/', AvailableJobDeleteView.as_view, name = 'deletejob'),
    path('delete/<int:pk>/worker/', AvailableWorkerDeleteView.as_view, name = 'deleteworker'),
    path('delete/<int:pk>/tool/', FarmToolDeleteView.as_view, name = 'deletetool'),
    #home items detail urls
    path('advert/<int:pk>/detail/', AdvertDetailView.as_view(), name = 'advertdetail'),
    path('trending/<int:pk>/detail/', TrendingDetailView.as_view(), name = 'trendingdetail'),
    path('land/<int:pk>/detail/', LandDetailView.as_view(), name = 'landdetail'),
    path('worker/<int:pk>/detail/', AvailableWorkerDetailView.as_view(), name = 'workerdetail'),
    path('job/<int:pk>/detail/', AvailableJobDetailView.as_view(), name = 'jobdetail'),
    path('farm/<int:pk>/tool/detail/', FarmToolsDetailView.as_view(), name = 'tooldetail'),
    #home list views
    path('advert/list/',AdvertListView.as_view(), name = 'advertlist'),
    path('trending/list/',TrendingListView.as_view(), name = 'trendinglist'),
    path('land/list/',LandListView.as_view(), name = 'landlist'),
    path('farm/tools/list/',FarmToolsListView.as_view(), name = 'toollist'),
    path('workers/list/',WorkerListView.as_view(), name = 'workerlist'),
    path('jobs/list/',JobListView.as_view(), name = 'joblist'),
]
