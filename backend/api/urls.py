from django.urls import path
from .views import hellow_world, CandidateFileViewSet

urlpatterns = [
    path("hello/", hellow_world),
    path("candidates/", CandidateFileViewSet.as_view({'get': 'list', 'post': 'create'})),
]
