
from typing import Generic
from rest_framework.response import Response
from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def job_list_api(request):
    job_list = Job.objects.all()
    data = JobSerializer(job_list,many=True).data
    return Response({'data':data})



@api_view(['GET'])
def job_details_api(request,id):
    job = Job.objects.get(id = id)
    data = JobSerializer(job).data
    return Response({'data':data})

class JobListApi(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailsApi(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field="id"
