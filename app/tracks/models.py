from django.db import models
from app.users import models as user_models


class TimeStampedModel(models.Model):

    """ Base Model """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Track(TimeStampedModel):

    """ Track Model """

    title = models.CharField(max_length=50)
    track = models.FileField(upload_to='tracks')
    creator = models.ForeignKey(
        user_models.User,
        on_delete=models.CASCADE,
        null=True,
        related_name='tracks'
    )

    @property
    def track_like_count(self):
        return self.track_likes.count()

    def __str__(self):
        return '{} - {}'.format(self.title, self.creator.name)


class Track_Like(models.Model):

    """ Track Like Model """

    creator = models.ForeignKey(
        user_models.User,
        on_delete=models.CASCADE,
        null=True,
        related_name='track_likes'
    )
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        null=True,
        related_name='track_likes'
    )

    def __str__(self):
        return 'Liked Track: {}'.format(self.track.title)