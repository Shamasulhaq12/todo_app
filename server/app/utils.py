import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(key, data):
    _data = str(data)
    encoded_data = pad(_data.encode(), AES.block_size)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(encoded_data)).decode('utf-8')

def decrypt(key, data):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(data)), AES.block_size).decode('utf-8')