from main import models
from main.tools import getNowTimeStamp
import requests
import json



def requestsGet(url, data={}):
    url += '?'
    for key, value in data.items():
        url += key + '=' + value + '&'
    res = requests.get(url[:-1])
    return res

def getAccessToken():
    config = models.OfficialAccount.objects.all().first()
    if config.access_token_expire_time >= getNowTimeStamp():
        return True, config.access_token_value
    res = requestsGet(
        'https://api.weixin.qq.com/cgi-bin/token', 
        {
            'grant_type': 'client_credential', 
            'appid': config.wxpay_appid, 
            'secret': config.wxpay_app_key
        }
    )
    if res.status_code == 200:
        resData = json.loads(res.text)
        config.access_token_value = resData['access_token']
        config.access_token_expire_time = resData['expires_in'] + getNowTimeStamp()
        config.save()
        return True, resData['access_token']
    return False, '获取accesstoken错误'
        
    
def getOpenid(code):
    config = models.OfficialAccount.objects.all().first()
    res = requestsGet(
        'https://api.weixin.qq.com/sns/oauth2/access_token', 
        {
            'grant_type': 'authorization_code', 
            'appid': config.wxpay_appid, 
            'secret': config.wxpay_app_key,
            'code': code
        }
    )
    if res.status_code == 200:
        resData = json.loads(res.text)
        return True, resData['openid']
    return False, '获取openid错误'