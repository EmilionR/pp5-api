from rest_framework import generics, permissions
from models import Block
from serializers import BlockSerializer
from drf_api.permissions import IsOwnerOrReadOnly


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

class BlockDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a block,
    if you're the owner, also delete the block
    """
    queryset = Block.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BlockSerializer
