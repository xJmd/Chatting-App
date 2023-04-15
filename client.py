import requests


req = requests.get('http://localhost:5000/ping')
print(req.json())

req_concept = {
    'action': 'get-messages',
    'user': 'testkey',
}