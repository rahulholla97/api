import requests
import json
input_from_api = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = input_from_api.text
aa=(json.loads(data))
print('Welcome world')
for k,v in aa.items():
    print(f"{k} is assigned to {v}")