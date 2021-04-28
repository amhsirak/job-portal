from django.urls import path

from .import views

urlpatterns = [
    path('' ,  views.index , name = 'jobs') ,
    path('<int:job_id>' , views.job , name = 'job') ,
    path('search' , views.search , name = 'search') ,
    path('applyjob<int:job_id>', views.applyjob, name='applyjob_with_job_id'),
]