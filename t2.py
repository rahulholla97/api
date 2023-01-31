import requests
import json
input_from_api = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = input_from_api.text
print(json.loads(data))
print('Hello TTM')