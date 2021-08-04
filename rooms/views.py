from typing import Union

from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from .models import Room, Schedule
from .serializers import RoomSerializer, ScheduleSerializer
from .permissions import IsOwnerOrReadOnly


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomSchedule(generics.ListCreateAPIView):
    serializer_class = ScheduleSerializer

    def _get_room(self):
        return get_object_or_404(Room, pk=self.kwargs['pk'])

    def get_queryset(self):
        room_schedule = Schedule.objects.filter(room=self._get_room())
        return room_schedule

    def perform_create(self, serializer):
        serializer.save(room=self._get_room(), user=self.request.user)


class ScheduleList(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnly]


class RootView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        content = {
            # 'users': reverse('user-list', request=request, format=format),
            'rooms': reverse('room-list', request=request),
            'schedule': reverse('schedule-list', request=request)
        }
        return Response(content)
