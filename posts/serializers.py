from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from reports.models import Report


class PostSerializer(serializers.ModelSerializer):
    """
    Serialize posts and retrieve relevant data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    report_id = serializers.SerializerMethodField()
    like_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()

    # Check if current user is the owner
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Get id of likes
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    # Get id of reports
    def get_report_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            report = Report.objects.filter(
                owner=user, post=obj
            ).first()
            return report.id if report else None
        return None

    # Validate image size
    def validate_image(self, value):
        # Check if the file is bigger than 2MB
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is over 2MB!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height exceeds 4096 pixels.'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width exceeds 4096 pixels.'
            )
        return value

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'friends_only', 'title', 'content', 'image', 'image_filter',
            'created_on', 'updated_on', 'like_id', 'report_id',
            'like_count', 'comment_count',
        ]
