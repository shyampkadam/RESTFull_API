import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'showallemp'
URL1 ="https://api.openweathermap.org/data/2.5/weather?q=pune&appid=637ea8e97f5bcbd8ae9675a6bd04dbd5"


resp = requests.get(URL1)
data = resp.json()
print(data)