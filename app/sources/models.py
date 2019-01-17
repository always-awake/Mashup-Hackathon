from django.db import models
from app.users import models as user_models
from app.tracks.models import TimeStampedModel


class Source(TimeStampedModel):

    """ Source Model """

    title = models.CharField(max_length=50)
    source = models.FileField(upload_to='sources')
    creator = models.ForeignKey(
        user_models.User,
        on_delete=models.CASCADE,
        null=True,
        related_name='sources'
    )
    image = models.ImageField(upload_to='sources/images') # 각 소스의 고유 이미지
    volume = models.IntegerField() # 트랙 내 유저가 저장한 소스 볼륨

    @property
    def source_like_count(self):
        return self.source_likes.count()

    def __str__(self):
        return '{} - {}'.format(self.title, self.creator.name)


class Source_Like(models.Model):

    """ Source Like Model """

    creator = models.ForeignKey(
        user_models.User,
        on_delete=models.CASCADE,
        null=True,
        related_name='track_likes'
    )
    source = models.ForeignKey(
        Source,
        on_delete=models.CASCADE,
        null=True,
        related_name='source_likes'
    )

    def __str__(self):
        return 'Liked Source: {}'.format(self.source.title)