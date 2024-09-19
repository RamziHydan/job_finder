from django.urls import path
from . import views
app_name= 'account'
urlpatterns=[
    path('signup',views.signup,name='signup'),    
    path('profile/', views.profile, name='profile'),
    path('pro/', views.pro, name='pro'),
    path('profile-edit/',views.profile_edit,name='profile-edit'),   
]