from django.db import models
from django.contrib.auth import get_user_model

from . import Room
from .time_stamped_model import TimeStampedModel

User = get_user_model()


class ScheduleStatus:
    NEW = 'N'
    RESERVED = 'R'
    CANCELLED = 'C'


STATUS = (
    (ScheduleStatus.NEW, 'New'),
    (ScheduleStatus.RESERVED, 'Reserved'),
    (ScheduleStatus.CANCELLED, 'Cancelled')
)


class Schedule(TimeStampedModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='schedule')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedule')
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    status = models.CharField(max_length=1, choices=STATUS, blank=True, default=ScheduleStatus.NEW)
    comment = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = '-date', '-time_start'

    def __str__(self):
        return f'{self.room.name}'

    class Fields:
        ID = 'id'
        ROOM = 'room'
        USER = 'user'
        DATE = 'date'
        TIME_START = 'time_start'
        TIME_END = 'time_end'
        STATUS = 'status'
        COMMENT = 'comment'
