from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CheckinSerializer
from .models import Checkin

# Create your views here.
class CheckinViewSet(viewsets.ModelViewSet):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
