from .models import CandidateFile
from .serializers import CandidateFileSerializer
from rest_framework import viewsets

class CandidateFileViewSet(viewsets.ModelViewSet):
    queryset = CandidateFile.objects.all()
    serializer_class = CandidateFileSerializer