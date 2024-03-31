from django.db import IntegrityError
from rest_framework import serializers
from .models import Friend


class FriendSerializer(serializers.ModelSerializer):
    """
    Serialize the Friend model,
    Add fields for displaying the details
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    friend_name = serializers.ReadOnlyField(source='friend.username')

    class Meta:
        model = Friend
        fields = [
            'id', 'owner', 'created_on', 'friend', 'friend_name'
        ]

    # Custom create method to ensure only one instance of each pairing
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
