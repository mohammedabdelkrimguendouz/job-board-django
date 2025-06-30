
from django.urls import path

from . import views
from . import api

app_name = 'job'

urlpatterns = [
    path('', views.job_list ,name='job_list'),
    path('add', views.add_job,name='add_job'),
    path('<str:slug>', views.job_details,name='job_details'),

    #api FBV
    path('api/v1/jobs', api.job_list_api,name='job_list_api'),
    path('api/v1/jobs/<int:id>', api.job_details_api,name='job_list_api'),


    #api CBV
    path('api/v2/jobs', api.JobListApi.as_view(),name='job_list_api'),
    path('api/v2/jobs/<int:id>', api.JobDetailsApi.as_view(),name='job_list_api'),


]