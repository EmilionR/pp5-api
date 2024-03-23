from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListAPIView):
    """
    List all Post instances
    """
    queryset = Post.objects.annotate(
        like_count=Count('likes', distinct=True),
        comment_count=Count('comment', distinct=True)
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'like_count',
        'comment_count',
        'like__created_on',
    ]

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Associate the post with signed-in user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post
    if owner, edit or delete it
    """
    queryset = Post.objects.annotate(
        like_count=Count('likes', distinct=True),
        comment_count=Count('comment', distinct=True)
    ).order_by('-created_on')

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
