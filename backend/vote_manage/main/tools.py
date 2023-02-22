import hashlib
import time
import re

# 验证类，通过addCheck()增加验证规则，start()进行统一验证
class Validate:
    def __init__(self):
        self.funList = []
        self.dataList = []
        self.msgList = []

    def clear(self):
        self.funList.clear()
        self.dataList.clear()
        self.msgList.clear()

    def start(self):
        ok = True
        for i in range(len(self.funList)):
            ok = ok and getattr(self, self.funList[i], None)(self.dataList[i])
            if not ok:
                self.clear()
                return False, self.msgList[i]
        self.clear()
        return True, 'ok'

    def addCheck(self, fun, data, msg):
        if not hasattr(self, fun):
            return False
        self.funList.append(fun)
        self.dataList.append(data)
        self.msgList.append(msg)
        return True

    def isEmpty(self, data):
        if data is None or len(str(data)) <= 0:
            return False
        return True

    def maxLength(self, data, length=20):
        data = str(data)
        return len(data) <= length

    def minLength(self, data, length=0):
        data = str(data)
        return len(data) >= length

    def minValue(self, data, minValue=0):
        data = int(data)
        return data >= minValue
    
    def maxValue(self, data, maxValue=0):
        data = int(data)
        return data <= maxValue

    def isEmail(self, data):
        return re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", data) != None

    def hasSpace(self, data):
        return str(data).find(' ') != -1 or str(data).find('\t') != -1

    def isOnlyNumal(self, data):
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
    return int(time.time)