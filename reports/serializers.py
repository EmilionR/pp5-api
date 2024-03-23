from .models import Report
from rest_framework import serializers


class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer for Report model
    Adds three additional fields returning a list of Report instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Report
        fields = [
            'id', 'owner', 'content', 'post', 'created_on', 'updated_on'
        ]


class ReportDetailSerializer(ReportSerializer):
    """
    Serializes the Report model for Detail view
    Has an additional post field
    Post is read-only and so does not need to be set on each update
    """
    post = serializers.ReadOnlyField(source='post.id')