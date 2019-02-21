from django.contrib import admin
from . import models


@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'creator',
    )


@admin.register(models.TrackLike)
class TrackLikeAdmin(admin.ModelAdmin):
    list_display = (
        'track',
        'user',
    )
