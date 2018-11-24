from django.db import models


class Track(models.Model):

    """ Track Model """

    title = models.CharField(max_length=50)
    track = models.FileField(upload_to='tracks')

    