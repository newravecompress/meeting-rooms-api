from django.contrib import admin

from .models import Room, Schedule


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (Room.Fields.ID, Room.Fields.NAME, Room.Fields.NUM_CHAIRS, Room.Fields.HAS_PROJECTOR,
                    Room.Fields.HAS_DESK, 'added', 'edited')

    fields = (Room.Fields.NAME, Room.Fields.NUM_CHAIRS, Room.Fields.HAS_PROJECTOR,
              Room.Fields.HAS_DESK)

    readonly_fields = 'added', 'edited'


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (Schedule.Fields.ID, Schedule.Fields.ROOM, Schedule.Fields.DATE, Schedule.Fields.TIME_START,
                    Schedule.Fields.TIME_END, Schedule.Fields.USER, Schedule.Fields.STATUS, 'added', 'edited')

    readonly_fields = 'added', 'edited'
