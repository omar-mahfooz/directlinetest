from django.shortcuts import render, HttpResponse

from .models import Total
from rest_framework import viewsets
from .serializers import TotalSerializer

# Create your views here.

class TotalViewSet(viewsets.ModelViewSet):
    queryset = Total.objects.all()
    serializer_class = TotalSerializer
    model = Total











