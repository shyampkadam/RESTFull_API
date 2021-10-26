import requests
import json
URL ="http://localhost:8000/empcreate/"

emp={
    'name':'shyam',
    'age':25,
    'city':'pune'
}

json_data=json.dumps(emp)

responsedata=requests.post(url=URL,data=json_data)

data = responsedata.json()

print(data)

