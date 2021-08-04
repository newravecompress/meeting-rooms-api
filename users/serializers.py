from django.contrib.auth import get_user_model
from rest_framework import serializers

from rooms.models import Room, Schedule


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # rooms = serializers.HyperlinkedRelatedField(many=True, view_name='room-detail', read_only=True)
    # schedule = serializers.HyperlinkedRelatedField(many=True, view_name='schedule')

    class Meta:
        model = get_user_model()
        fields = 'id', 'url', 'email'
