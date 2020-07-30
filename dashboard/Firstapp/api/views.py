from rest_framework import viewsets 
from Firstapp.models import ITJobs,MECHJobs
from Firstapp.api.serializers import ITJobsSerializer ,MECHJobsSerializer
class ITJobsCRUDCBV(viewsets.ModelViewSet):
    serializer_class=ITJobsSerializer 
    queryset=ITJobs.objects.all()

class MECHJobsCRUDCBV(viewsets.ModelViewSet):
    serializer_class=MECHJobsSerializer 
    queryset=MECHJobs.objects.all()