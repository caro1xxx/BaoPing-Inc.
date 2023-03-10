import json
import requests
import hashlib
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization, hashes
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# 步骤三 下单
def transactions():
    url = 'https://api.mch.weixin.qq.com/v3/pay/transactions/jsapi'
    headers = {
        'content-type': 'application/json'
    }
    data = {
        "mchid": "1900006XXX",
        "out_trade_no": "1217752501201407033233368318",
        "appid": "wxdace645e0bc2cXXX",
        "description": "Image形象店-深圳腾大-QQ公仔",
        "notify_url": "https://www.weixin.qq.com/wxpay/pay.php",
        "amount": {
            "total": 1,
            "currency": "CNY"
        },
        "payer": {
            "openid": "o4GgauInH_RCEdvrrNGrntXDuXXX"
        }
    }
    # print(json.dumps(data))
    res = requests.post(url, data=data, headers=headers)
    # print(json.dumps(res))
    if res.status_code == 200:
        prepayId = res['prepay_id']
        return True, prepayId
    return False, 'error'

def generateSignData():
    appId = 'wx8888888888888888'
    timeStamp = '1414561699'
    nonceStr = '5K8264ILTKCH16CQ2502SI8ZNMTM67VS'
    prepayId = 'wx201410272009395522657a690389285100 '
    package = 'prepay_id=' + prepayId

    text = appId + '\n' + timeStamp + '\n' + nonceStr + '\n' +  + '\n' + package + '\n'
    return text

def getSign(data):
    # 生成RSA密钥对
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    # 序列化私钥以便存储
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    print(private_key_pem)
    # 要签名的数据
    # data = b"Hello, world!"
    # 计算SHA256散列值
    digest = hashlib.sha256(data).digest()
    # 使用RSA私钥对SHA256散列进行签名
    signature = private_key.sign(
        digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
    # 将签名结果进行Base64编码
    signature_base64 = base64.b64encode(signature).decode('utf-8')
    return signature_base64

sign = getSign(generateSignData())
print(sign)

# decrypted_str = decrypt("要解密的字符串", "私钥文件路径")
def decrypt(ciphertext, private_key_path):
    with open(private_key_path, "rb") as f:
        private_key = f.read()
    # 使用RSA私钥解密数据
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    cipherdata = base64.b64decode(ciphertext.encode())
    decrypted = cipher.decrypt(cipherdata)

    return decrypted.decode()

def queryOrderStatus(self):
    out_trade_no = '1217752501201407033233368018'
    mchid = '1230000109'
    url = 'https://api.mch.weixin.qq.com/v3/pay/transactions/out-trade-no/'
    url += '{}?mchid={}'.format(out_trade_no, mchid)
    res = requests.get(url)
    if res.status_code == 200:
        return True, res
    return False, 'query status error'


# 步骤八 调起支付 签名
def arousePay():
    text = generateSignData()
    signText = getSign(text)
    data = {
        "appId": "wx2421b1c4370ec43b",          
        "timeStamp": "1395712654",     
        "nonceStr": "e61463f8efa94090b1f366cccfbbb444",    
        "package": "prepay_id=up_wx21201855730335ac86f8c43d1889123400",
        "signType": "RSA",        
        "paySign": signText
    }
    return data



# print(getSign())