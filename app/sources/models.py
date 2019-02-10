from django.conf import settings
from django.db import models
from tracks.models import TimeStampedModel


class Source(TimeStampedModel):
    """ Source Model """
    title = models.CharField(max_length=50)
    source = models.FileField(upload_to='sources')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='sources'
    )
    # 각 소스의 고유 이미지
    image = models.ImageField(upload_to='sources/images')
    # 트랙 내 유저가 저장한 소스 볼륨
    volume = models.IntegerField()

    @property
    def like_count(self):
        return self.sourcelikes.count()

    def __str__(self):
        return f'{self.title} - {self.creator.name}'


class SourceLike(models.Model):
    """ Source Like Model """
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='sourcelikes'
    )
    source = models.ForeignKey(
        Source,
        on_delete=models.CASCADE,
        null=True,
        related_name='sourcelikes'
    )

    def __str__(self):
        return f'Liked Source: {self.source.title}'
