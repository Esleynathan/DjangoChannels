from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/app/(?P<nome>\w+)/$', consumers.TesteConsumer.as_asgi()),
]