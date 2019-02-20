from django.urls import path

from . import apis

app_name = "tracks"
urlpatterns = [
    path('', apis.TrackListAPIView.as_view(), name='track_list'),
    path('tracks/', apis.TrackCreateAPIView.as_view(), name='creat_track'),
    path('<int:track_id>/likes/', apis.TrackLikeCreateAPIView.as_view(), name='like_track'),
]
