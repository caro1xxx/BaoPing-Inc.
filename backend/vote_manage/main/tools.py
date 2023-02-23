import hashlib
import time
import re
import random
import string

# 验证类，通过addCheck()增加验证规则，start()进行统一验证
# 验证类的check开头的方法，如果验证通过为True，否则为False
class Validate:
    def __init__(self):
        self.funList = []
        self.dataList = []
        self.msgList = []
        self.checkValueList = []

    def clear(self):
        self.funList.clear()
        self.dataList.clear()
        self.msgList.clear()
        self.checkValueList.clear()

    def startCheck(self):
        ok = True
        for i in range(len(self.funList)):
            if self.checkValueList[i] is None:
                ok = ok and getattr(self, self.funList[i], None)(self.dataList[i])
            else:
                ok = ok and getattr(self, self.funList[i], None)(self.dataList[i], self.checkValueList[i])
            if not ok:
                msg = self.msgList[i]
                self.clear()
                return False, msg
        self.clear()
        return True, 'ok'

    def addCheck(self, fun, data, msg, checkValue=''):
        if not hasattr(self, fun):
            return False
        self.funList.append(fun)
        self.dataList.append(data)
        self.msgList.append(msg)
        self.checkValueList.append(checkValue)
        return True

    def checkIsNotEmpty(self, data, *args):
        if data is None or len(str(data)) <= 0:
            return False
        return True

    def checkMaxLength(self, data, length=20):
        data = str(data)
        return len(data) <= length

    def checkMinLength(self, data, length=0):
        data = str(data)
        return len(data) >= length

    def checkMinValue(self, data, minValue=0):
        data = int(data)
        return data >= minValue
    
    def checkMaxValue(self, data, maxValue=0):
        data = int(data)
        return data <= maxValue

    def checkIsEmail(self, data, *args):
        return re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", data) != None

    def checkHasNoSpace(self, data, *args):
        return str(data).find(' ') == -1 and str(data).find('\t') == -1

    def checkOnlyNumal(self, data):
        return data.isalnum()


# Validate使用过程
# ck = Validate()
# data = 30
# ck.addCheck('empty', data, 'null')
# ck.addCheck('maxLength', data, 'maxlength')
# print(ck.start())


def genearteMD5(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    # print(md5.hexdigest())
    return md5.hexdigest()

def getNowTimeStamp():
    return int(time.time())

def generateString16():
    # random.sample('1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()', 16)
    randStr = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    return randStr

def generateCode6():
    randStr = ''.join(random.sample(string.digits, 6))
    return randStr