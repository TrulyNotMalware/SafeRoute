from django.shortcuts import render
from rest_framework import generics
from .models import Subway
from .serializer import RequestSerializer

# Create your views here.
class RequestList(generics.ListCreateAPIView):
    queryset = Subway.objects.all()
    serializer_class = RequestSerializer

class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subway.objects.all()
    serializer_class = RequestSerializer