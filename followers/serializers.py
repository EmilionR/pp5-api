from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serialize the Follower model,
    Add fields for displaying the details
    """
    follower = serializers.ReadOnlyField(source='follower.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'follower', 'created_at', 'followed', 'followed_name'
        ]

    # Custom create method to ensure only one instance of each pairing
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})