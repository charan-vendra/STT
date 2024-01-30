from django.urls import re_path
from .consumers import SpeechRecognitionConsumer

websocket_urlpatterns = [
    re_path(r'ws/speech-to-text/$', SpeechRecognitionConsumer.as_asgi()),
]
