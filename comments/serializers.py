from .models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment model
    Adds three additional fields returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_pic = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_pic',
            'content', 'post', 'created_on', 'updated_on'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializes the Comment model for Detail view
    Has an additional post field
    Post is read-only and so does not need to be set on each update
    """
    post = serializers.ReadOnlyField(source='post.id')