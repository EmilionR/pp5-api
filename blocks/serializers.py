from rest_framework import serializers
from django.db import IntegrityError
from .models import Block


class BlockSerializer(serializers.ModelSerializer):
    """
    Serialize the Block model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    target = serializers.ReadOnlyField(source='target.username')

    # Create method that avoids duplicate blocks
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })

    class Meta:
        model = Block
        fields = ['id', 'owner', 'target', 'created_on']
