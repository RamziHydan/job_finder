from .serializers import JobSerializer
from .models import Job
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

## Get all jobs v1
@api_view(['GET'])
def job_list_apiv1(request):
    all_jobs =Job.objects.all()
    data=JobSerializer(all_jobs,many=True).data
    context={
        'data':data
    }
    return Response(context)


## Get one job v1
@api_view(['GET'])
def job_details_apiv1(request,id):
    job_details=Job.objects.get(id=id)
    data=JobSerializer(job_details).data
    context={
        'data':data
    }
    return Response(context)

## Get all jobs v2
class Job_list_apiv2(generics.ListCreateAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer

class Job_details_apiv2(generics.RetrieveUpdateDestroyAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer    
    lookup_field='id'