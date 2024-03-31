from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


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
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    # Filter criteria, based on database relations
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
        'owner__friend__owner__profile',
    ]
    # Fields by which to order profile
    ordering_fields = [
        'post_count',
        'follower_count',
        'following_count',
        'friend_count',
        'owner__following__created_on',
        'owner__followed__created_on',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail view of a single profile
    If owner, update or delete the profile
    """
    queryset = Profile.objects.annotate(
        post_count=Count('owner__post', distinct=True),
        follower_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_on')
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    def perform_destroy(self, instance):
        # Delete the associated User instance
        instance.owner.delete()
        # Call the superclass method to delete the profile
        super().perform_destroy(instance)
