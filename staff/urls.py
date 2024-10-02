from django.urls import path
from .views import index, training_view, video_feed, detection_view

urlpatterns = [
    path("", index, name="index"),
    path("training/", training_view, name="training"),
    path('video_feed/', video_feed, name='video_feed'),
    path("detection/", detection_view, name="detection"),
]
