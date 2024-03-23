from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List of all profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Detail view of a single post
    If owner, update the profile
    """
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer