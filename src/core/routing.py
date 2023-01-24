# from channels.auth import AuthMiddleware
# from channels.routing import ProtocolTypeRouter, URLRouter

# import chat.routing

# application = ProtocolTypeRouter(
#     {
#         "websocket": AuthMiddleware(
#             URLRouter(
#                 chat.routing.websocket_urlpatterns
#             )
#         ),
#     }
# )
