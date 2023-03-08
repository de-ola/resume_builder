from django.shortcuts import render
from rest_framework import generics, status, permissions
from .models import Biodata, Projects
from user.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# Create your views here.
class BiodataCreateView(generics.ListCreateAPIView):
    queryset = Biodata.objects.all()
    serializer_class = BiodataSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, request):
        qs = super().get_queryset()
        if qs is not None:
            return qs.filter(user=request.user)
        else:
            return Projects.objects.none()
        
class BiodataEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Biodata.objects.all()
    serializer_class = BiodataSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def get_queryset(self, request):
        qs = super().get_queryset()
        if qs is not None:
            return qs.filter(user=request.user)
        else:
            return Biodata.objects.none()
        
class ProjectEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, request):
        qs = super().get_queryset()
        if qs is not None:
            return qs.filter(user=request.user)
        else:
            return Projects.objects.none()