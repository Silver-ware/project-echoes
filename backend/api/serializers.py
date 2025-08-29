from rest_framework import serializers
from .models import CandidateFile

class CandidateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateFile
        fields = ['id', 'repo_path', 'file_path', 'language', 'code', 'reviewed', 'approved']