from flask import request
import json
import secrets


class User:
    def login(self):
        @self.app.route('/login', methods=['POST'])
        def login():
            response = {'type': 'login', 'error':None}
            req = request.json
            enough_data = True
            
            try:
                user = self.handler.user.check_login(req['name'], req['password'])
            except KeyError:
                response['error'] = 'Not enough information provided! Requests must provide a username and password.'
                enough_data = False

            if enough_data:
                if user == False:
                    response['error'] = f'Either the user "{req["name"]}" does not exist or the password is incorrect.'
                else:
                    new_key = secrets.token_hex()
                    self.handler.user.edit(user['key'], 'key', new_key)
                    response['key'] = new_key

            return json.dumps(response)
        
    def signup(self):
        @self.app.route('/signup', methods=['POST'])
        def signup():
            response = {'type': 'signup', 'error':None}
            req = request.json
            enough_data = True
            
            try:
                name = req['name']
                password = req['password']
            except KeyError:
                response['error'] = 'Not enough information provided! Requests must provide a username and password.'
                enough_data = False

            if enough_data:
                no_duplicates = self.handler.user.add(name, password)
                if not no_duplicates: # If there is a duplicate user
                    response['error'] = f'The account: "{name}" already exists!'
                else:
                    user = self.handler.user.get_name(name)
                    response['key'] = user['key']


            return json.dumps(response)