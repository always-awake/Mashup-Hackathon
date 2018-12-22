from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ User Model """

    name = models.CharField("Name of User", blank=True, max_length=255)