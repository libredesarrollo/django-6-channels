from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async

from django.contrib.auth.models import AnonymousUser

@database_sync_to_async
def get_user(token_key):
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return None

def get_user_sesion(scope):
    user = scope.get("user")
    print(scope.get("user"))
    if user and user.is_authenticated:
        return user

    return AnonymousUser()
class TokenAuthMiddleware:
    def __init__(self, app):
        self.app = app
    async def __call__(self, scope, receive, send):
        token = scope['query_string'].decode('utf-8')
        if len(token.split('_')) == 2:
            token_name, token_key = token.split('_')
            if token_name=='Token':
                scope['user'] = await get_user(token_key)

        if scope['user'] == AnonymousUser:
            scope['user'] =  get_user_sesion(scope)
        return await self.app(scope, receive, send)