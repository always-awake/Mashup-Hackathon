from django.contrib import admin
from . import models


@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    
    pass
