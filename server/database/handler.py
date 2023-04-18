from .db import Database
from .user import User
from .chat import Chat

class Handler:
    def __init__(self):
        '''Initializes the Handler and the Database.'''

        self.db = Database('db.json')
        self.user = User(self.db)
        self.chat = Chat(self.db)
    


