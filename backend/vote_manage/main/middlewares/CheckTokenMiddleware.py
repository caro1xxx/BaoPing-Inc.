from django.utils.deprecation import MiddlewareMixin
from main.views.user.UserOp import UserOp
import json
from main import models
from main.views.user.UserOp import UserOp



class CheckTokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = json.loads(request.body).get('token', None)

        if token:
            userop = UserOp() 
            # userObj = models.User.objects.get(username=username)
            # serverToken, lastLoginTime = userop.getDataFromToken(userObj.token)
