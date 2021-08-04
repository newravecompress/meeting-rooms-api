from django.contrib import admin

from .models import Room, Schedule


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = 'id', 'room', 'date', 'user', 'status'
