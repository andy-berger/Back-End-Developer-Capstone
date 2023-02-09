from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import MenuItem, Booking, User
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all() 
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]