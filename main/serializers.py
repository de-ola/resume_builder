from rest_framework import serializers
from user.models import *
from .models import *

class BiodataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biodata
        fields = []

class ResumeSerializer(serializers.ModelSerializer):
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