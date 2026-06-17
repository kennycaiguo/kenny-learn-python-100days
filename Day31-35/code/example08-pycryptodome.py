"""
加密和解密
对称加密 - 加密和解密是同一个密钥 - DES / AES
非对称加密 - 加密和解密是不同的密钥 - RSA
pip install pycryptodome
注意：在代码中导包时，请使用 from Crypto.Cipher import AES 等大写的包名。
"""

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(key, plaintext):
    # key 必须是 16, 24 或 32 字节长
    cipher = AES.new(key, AES.MODE_CBC)
    # 使用 pad 对数据进行填充，并获取随机生成的 IV（初始向量）
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    # 返回 IV + 密文的 Base64 编码，便于存储和传输
    return base64.b64encode(cipher.iv + ct_bytes).decode('utf-8')

def aes_decrypt(key, ciphertext):
    ct_bytes = base64.b64decode(ciphertext.encode('utf-8'))
    iv = ct_bytes[:AES.block_size]      # 提取 IV
    ct = ct_bytes[AES.block_size:]       # 提取密文
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')

# 使用示例
key = b'16byteslongkey!!' # 必须严格满足 16、24 或 32 位
plaintext = "这是需要加密的机密信息"

encrypted = aes_encrypt(key, plaintext)
print("加密后:", encrypted)

decrypted = aes_decrypt(key, encrypted)
print("解密后:", decrypted)
