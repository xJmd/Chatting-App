import requests
import json
from time import time


class Client:
    def __init__(self):
        self.load_data()

    def load_data(self):
        base_data = {
            'url':'http://localhost:5000',
            'key': None,
            'cache': {}
        }
        try:
            file = open('client-data.json')
            self.data = json.load(file)
            file.close()
        except FileNotFoundError:
            file = open('client-data.json', 'w')
            file.write(
                json.dumps(base_data)
            )
            file.close()
            self.data = base_data
    
    def save_data(self):
        file = open('client-data.json', 'w')
        file.write(
            json.dumps(self.data)
        )
        file.close()
    
    def ping(self):
        req = requests.get(self.data['url'] + '/ping')
        return req.json()

    def send_req_raw(self, eurl, data):
        '''
        POSTs any json to the extended url
        (http://baseurl.com/extended/url)
        '''
        req = requests.post(self.data['url'] + eurl , json=data)
        return req.json()
    
    def login(self, name, password):
        data = {'name': name, 'password': password}
        res = self.send_req_raw('/login', data=data)
        if res['error'] == None:
            self.data['key'] = res['key']
            self.save_data()
        return res

    def signup(self, name, password):
        data = {'name': name, 'password': password}
        res = self.send_req_raw('/signup', data=data)
        if res['error'] == None:
            self.data['key'] = res['key']
            self.save_data()
        return res

    def send_message(self, chat_id, message):
        data = {
            'key': self.data['key'], 
            'action': 'send-message',
            'data': {'message': message}
        }
        res = self.send_req_raw('/chat/' + chat_id, data)
        return res
        

if __name__ == '__main__':
    client = Client()
    # client.login('Thbop', 'Beef64')
    chat_id = '098029348590'
    print(client.send_message(chat_id, 'Hello world!'))