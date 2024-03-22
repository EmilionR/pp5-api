from rest_framework import generics, permissions
from models import Block
from serializers import BlockSerializer


class BlockList(generics.ListCreateAPIView):
    """
    List of blocks
    if authenticated, create a like
    """
    queryset = Block.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlockSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    