from flask import request
import json

class Ping:
    def ping(self):
        @self.app.route('/ping')
        def ping():
            return '1'