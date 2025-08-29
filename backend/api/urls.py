from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import hellow_world, CandidateFileViewSet

router = DefaultRouter()
router.register(r'candidates', CandidateFileViewSet, basename='candidatefile')

urlpatterns = [
    path("hello/", hellow_world),
    path("candidates/", CandidateFileViewSet.as_view({'get': 'list', 'post': 'create'})),
]
