from main import models
from main.tools import Validate


class GiftOp:
    def checkGiftIsExist(self, pk):
        if models.Gift.objects.filter(pk=pk).first() is None:
            return False, '该礼物不存在'
        return True, None
    def checkDataOnCreate(self, data):
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data.get('name', None), '名称不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('value', None), '价值不能为空')
        validate.addCheck('checkIsNumber', data.get('value', None), '价值格式错误')
        validate.addCheck('checkIsNotEmpty', data.get('price', None), '价格不能为空')
        validate.addCheck('checkIsNumber', data.get('price', None), '价格格式错误')
        validate.addCheck('checkIsNotEmpty', data.get('status', None), '状态不能为空')
        validate.addCheck('checkIsNumber', data.get('status', None), '状态格式错误')
        ok, msg = validate.startCheck()
        return ok, msg
    
    def checkDataOnUpdate(self, data):
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data.get('pk', None), 'pk不能为空')
        validate.addCheck('checkIsNumber', data.get('pk', None), 'pk格式错误')
        validate.addCheck('checkIsNotEmpty', data.get('name', None), '名称不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('value', None), '价值不能为空')
        validate.addCheck('checkIsNumber', data.get('value', None), '价值格式错误')
        validate.addCheck('checkIsNotEmpty', data.get('price', None), '价格不能为空')
        validate.addCheck('checkIsNumber', data.get('price', None), '价格格式错误')
        validate.addCheck('checkIsNotEmpty', data.get('status', None), '状态不能为空')
        validate.addCheck('checkIsNumber', data.get('status', None), '状态格式错误')
        ok, msg = validate.startCheck()
        if not ok:
            return ok, msg
        
        ok, msg = self.checkGiftIsExist(data['pk'])
        if not ok:
            return ok, msg
        return True, None
    
    def create(self, data):
        models.Gift.objects.create(
            name = data['name'],
            value = data['value'],
            price = data['price'],
            status = data['status'],
            img = data['img'],
        ).save()


    def update(self, data):
        models.Gift.objects.filter(pk=data['pk']).update(
            name = data['name'],
            value = data['value'],
            price = data['price'],
            status = data['status'],
        )