import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'showallemp'
resp = requests.get(BASE_URL+ENDPOINT)
data = resp.json()
print(data)