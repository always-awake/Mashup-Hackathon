from rest_framework import serializers
from . import models


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Track
        fields = '__all__'


class TrackCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Track
        fields = (
            'title',
            'track',
        )
