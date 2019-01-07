import requests

url = 'http://localhost:8010/questions/api/'
headers = {'Authorization': 'Token e999e29469f997b7f8fd89673686bf1d78c2b81d'}
r = requests.get(url, headers=headers)
print(r.headers)
print(r.json())
