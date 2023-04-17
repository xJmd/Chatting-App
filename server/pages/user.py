from flask import request
import json
import secrets


class User:
    def login(self):
        @self.app.route('/login', methods=['POST'])
        def login():
            response = {'type': 'login', 'error':None}
            req = request.json
            
            user = self.handler.user.check_login(req['name'], req['password'])
            if user == False:
                response['error'] = f'Either the user "{req["name"]}" doesn\'t exist or the password is incorrect.'
            else:
                new_key = secrets.token_hex()
                self.handler.user.edit(user['key'], 'key', new_key)
                response['key'] = new_key

            return json.dumps(response)