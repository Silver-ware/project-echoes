from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CandidateFile
from .serializers import CandidateFileSerializer
from rest_framework import viewsets


@api_view(['GET'])
def hellow_world(request):
  return Response({"message": "Welcome!"})

class CandidateFileViewSet(viewsets.ModelViewSet):
    queryset = CandidateFile.objects.all()
    serializer_class = CandidateFileSerializer