from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework import generics

class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
       