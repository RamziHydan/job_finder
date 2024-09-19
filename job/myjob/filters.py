# import django_filters
# from django import forms
# from .models import Job
# class JobFilter(django_filters.FilterSet):
#     description = django_filters.CharFilter(lookup_expr='icontains')
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     location = django_filters.CharFilter(lookup_expr='icontains')
#     class Meta:
#         model = Job
#         fields = '__all__'
#         exclude=['onwer','image','vailable','slug','published_at',]
    


        # labels={
        #     'title':'',
        #     'location':'',
        #     'job_type':'',
        #     'description':'',
        #     'vacancy':'',
        #     'salary':'',
        #     'experience':'',
        #     'category':'',
        # }
        # widget ={
        #     'title':forms.TextInput(attrs={'class':'form-control valid','placeholder':'title'}) ,
        #     'location':forms.TextInput(attrs={'class':'form-control valid','placeholder':'location'}) ,
        #     'job_type':forms.Select(attrs={'class':'form-control valid','placeholder':'job_type'}) ,
        #     'description':forms.TextInput(attrs={'class':'form-control valid','placeholder':'description'}),
        #     'vacancy':forms.TextInput(attrs={'class':'form-control valid','placeholder':'vacancy'}) ,
        #     'salary':forms.TextInput(attrs={'class':'form-control valid','placeholder':'salary'}) , 
        #     'experience':forms.TextInput(attrs={'class':'form-control valid','placeholder':'experience'})  ,
        #     'category':forms.Select(attrs={'class':'form-control valid','placeholder':'category'}) , 
        # }