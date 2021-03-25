import requests

token='38a5906d99977101d13b4d27fa0162ec5105a8b4'
url='http://127.0.0.1:8000/api/project/'

response=requests.get(url,headers={'Authorization':f'Token {token}'})

print(response.status_code)
print(response.json())
