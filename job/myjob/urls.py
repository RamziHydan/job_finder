from django.urls import path
from . import views

from . import viewapi

from django.urls import path
from django.contrib import admin


urlpatterns=[
    path('admin/approval/', views.admin_approval, name='admin-approval'),
    path('job_list',views.job_list,name='job-list'),
    path('',views.index,name='index'),
    path('tag/<slug:tag_slug>/',views.job_list, name='job_list_by_tag'),
    path('add_job/',views.add_job,name='add-job'), 
    path('<str:slug>',views.job_details,name='job-details'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    ## v1 api with functions 
 
    path('api/list',viewapi.job_list_apiv1,name='job-list-api'),
    path('api/job/<int:id>',viewapi.job_details_apiv1,name='job-details-api'),

    ## v2 with generic class
    path('api/v2/list',viewapi.Job_list_apiv2.as_view(),name='job-list-api'),
    path('api/v2/job/<int:id>',viewapi.Job_details_apiv2.as_view(),name='job-details-api'),


]