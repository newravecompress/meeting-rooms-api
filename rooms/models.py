from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    num_chairs = models.PositiveSmallIntegerField()
    has_desk = models.BooleanField(blank=True, default=False)
    has_projector = models.BooleanField(blank=True, default=False)
    description = models.TextField(max_length=1000, blank=True)

    class Meta:
        ordering = 'name',

    def __str__(self):
        return self.name


class ScheduleStatus:
    NEW = 'N'
    RESERVED = 'R'
    CANCELLED = 'C'


class Schedule(models.Model):
    STATUS = (
        (ScheduleStatus.NEW, 'New'),
        (ScheduleStatus.RESERVED, 'Reserved'),
        (ScheduleStatus.CANCELLED, 'Cancelled')
    )

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
