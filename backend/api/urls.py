from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CandidateFileViewSet

router = DefaultRouter()
router.register(r'candidates', CandidateFileViewSet, basename='candidatefile')

urlpatterns = router.urls