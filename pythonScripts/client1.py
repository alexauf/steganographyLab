import requests

payload = {'msg': 'stego', 'pass': '123'}
r = requests.post("http://127.0.0.1:8000/shop", data=payload)
