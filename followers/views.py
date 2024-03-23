from rest_framework import generics, permissions
from .models import Follower
from .serializers import FollowerSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class FollowerList(generics.ListCreateAPIView):
    """
    List all instances of User following another User
    Create a follower-following pair if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    # Associate the signed-in user with a follower.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower
    If owner, delete a follower pair to unfollow someone
    """
    queryset = Follower.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
