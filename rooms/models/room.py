from django.db import models
from django.contrib.auth import get_user_model

from .time_stamped_model import TimeStampedModel

User = get_user_model()


class Room(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    num_chairs = models.PositiveSmallIntegerField()
    has_desk = models.BooleanField(blank=True, default=False)
    has_projector = models.BooleanField(blank=True, default=False)
    description = models.TextField(max_length=1000, blank=True)

    class Meta:
        ordering = 'name',

    def __str__(self):
        return f'{self.name}'

    class Fields:
        ID = 'id'
        NAME = 'name'
        NUM_CHAIRS = 'num_chairs'
        HAS_DESK = 'has_desk'
        HAS_PROJECTOR = 'has_projector'
        DESCRIPTION = 'description'
