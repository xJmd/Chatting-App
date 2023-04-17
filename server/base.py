from flask import Flask
from .database.handler import Handler

class BaseApp:
    def __init__(self, name):
        self.app = Flask(name)

        self.handler = Handler()

    def run(self, debug=False):
        self.app.run(debug=debug, host="0.0.0.0", port=5000)

