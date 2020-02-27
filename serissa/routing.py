from channels.routing import ProtocolTypeRouter, URLRouter
from recognitor.ws import routing as recognitor_routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(recognitor_routing.websocket_urlpatterns)
})
