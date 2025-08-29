from rest_framework import serializers
from .models import CandidateFile

class CandidateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateFile
        fields = '__all__'