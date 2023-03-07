from main import models
from main.tools import generateString16, getNowTimeStamp
import base64
from django.db.models import F


class KeysOp:
    def checkDataOnCreate(self, userAgent):
        if models.VoteUser.objects.filter(open_id=userAgent).first() is None:
            return False, '用户不存在'
        return True, None
    
    def generateKey(self):
        key = generateString16()
        return key

    def generateExpireTime(self):
        return getNowTimeStamp() + 5 * 60

    def create(self, userAgent):
        keysObj =  models.Keys.objects.create(
            value = self.generateKey(),
            expire_time = self.generateExpireTime(),
            user_agent_id = userAgent,
            has_used = 0
        )
        keysObj.save()
        return keysObj
    
    def checkKey(self, key):
        key = base64.b64decode(key.encode()).decode().replace('vote', '')
        keysObj = models.Keys.objects.filter(value=key).first()

        if keysObj is None:
            return False, 'key失效'
        if keysObj.expire_time < getNowTimeStamp() or keysObj.has_used != 0 :
            return False, 'key失效'
        
        keysObj.has_used = F('has_used') + 1
        keysObj.save()
        return True, 'ok'
