from rest_framework import generics, permissions
from likes.models import Like
from likes.serializers import LikeSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class LikeList(generics.ListCreateAPIView):
    """
    List of likes
    if authenticated, create a like
    """
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like,
    if you're the owner, also delete the like
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    