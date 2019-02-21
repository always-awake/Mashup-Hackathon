from django.conf import settings
from django.db import models


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
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='tracks'
    )

    @property
    def like_count(self):
        return self.tracklikes.all().count()

    def __str__(self):
        return f'{self.title} - {self.creator.username}'


class TrackLike(models.Model):
    """ Track Like Model """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='tracklikes'
    )
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        null=True,
        related_name='tracklikes'
    )

    def __str__(self):
        return f'{self.track.title} - {self.track.creator}'
