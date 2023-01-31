import requests
import json

fetched_data = requests.get('https://jsonplaceholder.typicode.com/todos/1')

data = json.loads(fetched_data.text)

for key,value in data.items():
    print(f"{key} = {value}")