


class Vaild:
    # 从request.body获取一个参数，并判断合法性
    def getParam(self, body, name, typeName='char'):
        res = json.loads(body).get(name, None)
        ok = False if not res else True
        if typeName == 'char':
            res = str(res)
        elif typeName == 'int':
            res = int(res)
        else:
            pass
        return res, ok
    
    def get500info(self):
        return {'code': 500, 'msg': 'Timeout'}

    def dataIsExist(self, ):
        pass