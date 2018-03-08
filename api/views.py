from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

class CreateView(generics.ListCreateAPIView):
    """Defines create behavior of api"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Defines GET, PUT, DELET behavior of api"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
