from django.urls import path

from .consumers import ProjectInfoConsumer

websocket_urlpatterns = [
    path("ws/projects/<int:pk>/$", ProjectInfoConsumer.as_asgi()),
]