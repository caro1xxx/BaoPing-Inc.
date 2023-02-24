from Crypto.Cipher import AES


 #创建一个aes对象
# # AES.MODE_CBC 表示模式是CBC模式
# en_text = aes.encrypt(text) 
# print("密文：",en_text) #加密明文，bytes类型
# aes = AES.new(password,AES.MODE_CBC,iv) #CBC模式下解密需要重新创建一个aes对象
# den_text = aes.decrypt(en_text)
# # print(str(en_text, 'utf-8'))
# print("明文：",den_text)



import time
def getNowTimeStamp():
    return int(time.time())

class AesOp:
    def __init__(self):
        self.password = b'1234567812345678' #秘钥，b就是表示为bytes类型
        self.iv = b'1234567812345678' # iv偏移量，bytes类型

    def addTo32(self, text):
        if len(text) < 32:
            text = text + ((32 - len(text)) * '=')
        return text

    def aesEncode(self, text):
        aes = AES.new(self.password, AES.MODE_CBC, self.iv)
        return aes.encrypt(text) 

    def aesDecode(self, text):
        aes = AES.new(self.password, AES.MODE_CBC, self.iv) #CBC模式下解密需要重新创建一个aes对象
        return str(aes.decrypt(text), 'utf-8').replace('=', '')
    

token = 'xiaotest' + ' ' + str(getNowTimeStamp())
aesOp = AesOp()
print(token)
token = aesOp.addTo32(token)
print(token)
token = aesOp.aesEncode(token)
print(token)
token = aesOp.aesDecode(token)
print(token)


