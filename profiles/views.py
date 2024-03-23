from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count

class ProfileList(generics.ListAPIView):
    """
    List of all profiles
    """
    # Annotate queryset to get counts of certain relations
    queryset = Profile.objects.annotate(
        post_count=Count('owner__post', distinct=True),
        follower_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        friend_count=Count('owner__friend', distinct=True)
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
    # Filter and order fields
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'post_count',
        'follower_count',
        'following_count',
        'friend_count',
        'owner__following__created_on',
        'owner__followed__created_on',
    ]

    

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Detail view of a single post
    If owner, update the profile
    """
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer