from rest_framework import serializers
from django.db import IntegrityError
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serialize the Like model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    # Create method that avoids duplicate likes
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })

    class Meta:
        model = Like
        fields = ['id', 'owner', 'post', 'created_on']
