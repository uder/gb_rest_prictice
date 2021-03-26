import requests
import json

url = 'http://127.0.0.1:8000/api-jwt-auth/'
user = 'devel'
password = 'dev123456!'


response = requests.post(url, data=json.dumps({'username': user, 'password': password}), headers={'Content-Type': 'application/json'})

print(response.status_code)
print(response.json())
