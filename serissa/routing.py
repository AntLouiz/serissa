from channels.routing import ProtocolTypeRouter, URLRouter
from recognitor.ws.routing import websocket_urlpatterns as recognitor
from trainings.ws.routing import websocket_urlpatterns as routing


websocket_urlpatterns = recognitor + routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns)
})
