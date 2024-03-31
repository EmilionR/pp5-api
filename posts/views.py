from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class PostList(generics.ListCreateAPIView):
    """
    List all Post instances
    """
    queryset = Post.objects.annotate(
        like_count=Count('likes', distinct=True),
        comment_count=Count('comment', distinct=True),
        report_count=Count('report', distinct=True)
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    # Filter criteria, based on database relations
    filterset_fields = [
        'owner__profile',
        'owner__followed__owner__profile',
        'likes__owner__profile',
    ]
    # Fields that are queried when searching
    search_fields = [
        'owner__username',
        'title',
    ]
    # Fields by which to order posts
    ordering_fields = [
        'like_count',
        'comment_count',
        'report_count',
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
