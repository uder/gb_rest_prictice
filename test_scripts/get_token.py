import requests

url='http://127.0.0.1:8000/api-token-auth/'
user='devel'
password='dev123456!'


response = requests.post(url, data={'username': user, 'password': password})

print(response.status_code)
print(response.json())