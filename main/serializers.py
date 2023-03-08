from rest_framework import serializers
from user.models import *
from .models import *

class BiodataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biodata
        fields = ['__all__']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['__all__']

class ResumeSerializer(serializers.ModelSerializer):
    biodata = BiodataSerializer(read_only=True)
    projects = ProjectSerializer(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'biodata',
            'projects',
        ]