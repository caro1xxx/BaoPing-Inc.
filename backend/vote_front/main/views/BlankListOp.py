from main import models


class BlankListOp:
    def addVoteUser(self, openId):
        models.BlackList.objects.create(open_id=openId)

    def addIp(self, ip):
        models.BlackList.Objects.create(ip=ip)

    def checkVoteUserIsExist(self, openId):
        if models.BlackList.objects.filter(open_id=openId).first() is None:
            return False
        return True

    def checkIpIsExist(self, ip):
        if models.BlackList.objects.filter(ip=ip).first() is None:
            return False
        return True