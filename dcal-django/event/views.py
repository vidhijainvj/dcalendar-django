from django_filters.rest_framework import DjangoFilterBackend


from django.shortcuts import render
from rest_framework import viewsets
from .serializers import eventSerializer
from .models import event

# Create your views here.

class eventView(viewsets.ModelViewSet):
    model = event
    serializer_class = eventSerializer
    queryset = event.objects.all()


    filter_fields = ('date')
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['date']


    #def get_queryset(self):
        
        #datee=self.request.query_params.get('date')
        #if datee is not None:
         #   queryset = event.objects.filter(date=datee)
        #return queryset