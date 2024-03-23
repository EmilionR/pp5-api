from rest_framework import generics, permissions
from .models import Friend
from .serializers import FriendSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class FriendList(generics.ListCreateAPIView):
    """
    List all instances of User friending another User
    Create a friend pair if logged in.
    """
    queryset = Friend.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FriendSerializer

    # Associate the signed-in user with a follower.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FriendDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a friend
    If owner, delete a Friend instance to unfriend someone
    """
    queryset = Friend.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FriendSerializer
