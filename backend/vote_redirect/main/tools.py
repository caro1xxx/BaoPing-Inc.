

# 验证类，通过addCheck()增加验证规则，start()进行统一验证
class Validate:
    def __init__(self):
        self.funList = []
        self.dataList = []
        self.msgList = []

    def start(self):
        ok = True
        for i in range(len(self.funList)):
            ok = ok and getattr(self, self.funList[i], None)(self.dataList[i])
            if not ok:
                return False, self.msgList[i]
        return True, 'ok'

    def addCheck(self, fun, data, msg):
        if not hasattr(self, fun):
            return False
        self.funList.append(fun)
        self.dataList.append(data)
        self.msgList.append(msg)
        return True

    def empty(self, data):
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


# Validate使用过程
# ck = Validate()
# data = 30
# ck.addCheck('empty', data, 'null')
# ck.addCheck('maxLength', data, 'maxlength')

# print(ck.start())