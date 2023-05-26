from django.urls import path
from hackathon.views import (
    HackathonListCreateAPIView,
    HackathonRetrieveUpdateAPIView,
    UserHackathonListAPIView,
    UserSubmissionListAPIView,
)

urlpatterns = [
    path('hackathons/', HackathonListCreateAPIView.as_view(), name='hackathon-list-create'),
    path('hackathons/<int:pk>/', HackathonRetrieveUpdateAPIView.as_view(), name='hackathon-retrieve-update'),
    path('user/hackathons/', UserHackathonListAPIView.as_view(), name='user-hackathon-list'),
    path('user/hackathons/<int:hackathon_id>/submissions/', UserSubmissionListAPIView.as_view(), name='user-submission-list-create'),
]
