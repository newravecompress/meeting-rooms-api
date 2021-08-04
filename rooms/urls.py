from django.urls import path

from . import views

urlpatterns = [
    path('', views.RootView.as_view()),
    path('rooms/', views.RoomList.as_view(), name='room-list'),
    path('rooms/<int:pk>/', views.RoomDetail.as_view(), name='room-detail'),
    path('rooms/<int:pk>/schedule/', views.RoomSchedule.as_view(), name='room-schedule'),

    path('schedule/', views.ScheduleList.as_view(), name='schedule-list'),
    path('schedule/<int:pk>/', views.ScheduleDetail.as_view(), name='schedule-detail'),
]
