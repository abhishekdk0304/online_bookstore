from django.shortcuts import render
from .serializers import BookstoreSerializer
from .models import Bookstore
from rest_framework import viewsets
# Create your views here.

class BookstoreViewSet(viewsets.ModelViewSet):
    queryset = Bookstore.objects.all()
    serializer_class = BookstoreSerializer
    