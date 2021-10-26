import requests

URL1 = "http://localhost:8000/stuinfo/1"
URL2 = "http://localhost:8000/allstuinfo/"

response = requests.get(url=URL2)

data = response.json()

print(data)