import json
import hashlib

dict = {
    "test":"test"
# Тело запроса
}

sha = hashlib.sha256(f'#секретный_ключ_для_шифрования{json.dumps(dict)}'.encode())
print(sha.hexdigest())
