from datetime import datetime
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Room, Schedule

User = get_user_model()


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = 'id', 'name', 'num_chairs', 'has_desk', 'has_projector', 'description'


class ScheduleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    room = serializers.ReadOnlyField(source='room.name')

    def validate(self, data):
        if data['time_end'] <= data['time_start']:
            raise serializers.ValidationError('Finish must occur after start')
        if data['date'] < datetime.now().date():
            raise serializers.ValidationError('Date cannot be in the past')
        return data

    class Meta:
        model = Schedule
        fields = 'id', 'url', 'room', 'user', 'date', 'time_start', 'time_end', 'status', 'comment'
        read_only_fields = 'status',


class ScheduleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = 'status',
