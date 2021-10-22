import requests
import json
URL = "http://localhost:8000/stucreate/"

student_data={
    'name':'shyam',
    'roll':101,
    'city':'pune'
}

json_data = json.dumps(student_data)

response = requests.post(url=URL,data=json_data)

data=response.json()
print(data)