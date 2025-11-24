from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChallengeViewSet, ChallengeCopyViewSet, SubmissionViewSet

router = DefaultRouter()
router.register(r'challenges', ChallengeViewSet, basename='challenge')
router.register(r'copies', ChallengeCopyViewSet, basename='challenge-copy')
router.register(r'submissions', SubmissionViewSet, basename='submission')

urlpatterns = [
    path('', include(router.urls)),
]
