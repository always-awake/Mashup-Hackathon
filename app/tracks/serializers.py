from rest_framework import serializers

from .models import Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = (
            'id',
            'created_at',
            'title',
            'track',
            'creator',
            'like_count',
        )


class TrackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = (
            'title',
            'track',
        )
