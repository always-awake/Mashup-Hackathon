from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


class TrackListAPIView(APIView):

    def get(self, request, format=None):

        tracks = models.Track.objects.all()

        serializer = serializers.TrackSerializer(tracks, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TrackCreateAPIView(APIView):

    def post(self, request, format=None):

        user = request.user

        serializer = serializers.TrackCreateSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(creator=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrackLikeCreateAPIView(APIView):

    def post(self, request, track_id, format=None):

        user = request.user

        try:
            found_track = models.Track.objects.get(id=track_id)
        except models.Track.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisiting_like = models.TrackLike.objects.get(
                user=user,
                track=found_track
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        except models.TrackLike.DoesNotExist:
            new_like = models.TrackLike.objects.create(
                user=user,
                track=found_track
            )
            new_like.save()
            return Response(status=status.HTTP_201_CREATED)