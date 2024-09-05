import os
import json
import base64
from Crypto.Cipher import AES

class hCaptcha:

    def __init__(self, version: str = "6c2596db2ce08d2f8763801d158624c790db3d34b0235bb33999fd85979fac64") -> None:
        self.key_chain = {
            "6c2596db2ce08d2f8763801d158624c790db3d34b0235bb33999fd85979fac64": [57, 193, 86, 78, 153, 197, 48, 29, 30, 110, 66, 69, 142, 163, 29, 31,158, 85, 63, 51, 59, 157, 80, 43,198, 155, 22, 23, 170, 244, 181, 109],
            "d1285730e6df7d9e9b8c090abc80b36cbbf8722e3655a8d303e084cc7824831a": [208, 37, 218, 11, 6, 85, 42, 133, 191, 44, 194, 245, 8, 152, 47, 32, 135, 246, 54, 205, 137, 131, 85, 50, 158, 226, 135, 163, 17, 60, 22, 0] # other version :)
        }

        if version not in self.key_chain:
            raise ValueError("Invalid version")
        
        self.key = bytes(self.key_chain[version])

    def decrypt(self, data: str) -> dict:
        data = base64.b64decode(data) 

        cipher = AES.new(self.key, AES.MODE_GCM, data[-13:-1])
        result = cipher.decrypt(data[:-13][:-16])  

        return json.loads(result)

    def encrypt(self, data: dict) -> str:
        json_data = json.dumps(data).encode()
        
        nonce = os.urandom(12)
        cipher = AES.new(self.key, AES.MODE_GCM, nonce)
        cipher_text, tag = cipher.encrypt_and_digest(json_data)
        
        result = cipher_text + tag + nonce + b"0"
        return base64.b64encode(result).decode()
