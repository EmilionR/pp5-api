from rest_framework import generics, permissions
from likes.models import Like
from likes.serializers import LikeSerializer


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

