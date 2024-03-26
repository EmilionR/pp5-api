from rest_framework import serializers
from .models import Profile
from followers.models import Follower
from friends.models import Friend
from blocks.models import Block

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    friend_id = serializers.SerializerMethodField()
    block_id = serializers.SerializerMethodField()
    post_count = serializers.ReadOnlyField()
    follower_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    friend_count = serializers.ReadOnlyField()

    # Check if current user is the owner
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    # Get id of followed user
    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None
    
    # Get id of friend
    def get_friend_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            friend = Friend.objects.filter(
                owner=user, friend=obj.owner
            ).first()
            return friend.id if friend else None
        return None
    
    # Get id of blocked user
    def get_block_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            block = Block.objects.filter(
                owner=user, target=obj.owner
            ).first()
            return block.id if block else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name', 'content',
            'image', 'is_owner', 'friend_id', 'following_id', 'block_id',
            'post_count', 'follower_count', 'following_count', 'friend_count',
        ]