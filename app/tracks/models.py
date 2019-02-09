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
        # User를 ForeignKey, ManyToMany, OneToOne에 사용시 settings.AUTH_USER_MODEL사용
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='tracks'
    )

    @property
    def like_count(self):
        # Track인스턴스의 속성이므로 property명에서 'track_'은 빼도 될 것 같음
        return self.track_likes.count()

    def __str__(self):
        # f-string을 써보자
        return f'{self.title} - {self.creator.name}'


# 클래스명에는 언더스코어 사용안함
class Track_Like(models.Model):
    """ Track Like Model """
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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
        # f-string을 써보자
        return f'Liked Track: {self.track.title}'
