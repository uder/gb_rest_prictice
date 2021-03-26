import requests
import json

#GET JWT
url = 'http://127.0.0.1:8000/api-jwt-auth/'
user = 'devel'
password = 'dev123456!'

response = requests.post(url, data=json.dumps({'username': user, 'password': password}), headers={'Content-Type': 'application/json'})
jwt=response.json()['access']
jwt_refresh=response.json()['refresh']

print('GET JWT')
print(response.status_code)
print(response.json())

#REFRESH JWT
url = 'http://127.0.0.1:8000/api-jwt-auth/refresh/'
response = requests.post(url, data=json.dumps({'refresh': jwt_refresh}), headers={'Content-Type': 'application/json'})
jwt=response.json()['access']

print('REFRESH JWT')
print(response.status_code)
print(response.json())

#GET PROJECTS
url='http://127.0.0.1:8000/api/project/'

response = requests.get(url,headers={'Authorization':f'Bearer {jwt}'})

print('GET PROJECTS')
print(response.status_code)
print(response.json())