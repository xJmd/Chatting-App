from .db import Database
from .user import User

class Handler:
    def __init__(self):
        '''Initializes the Handler and the Database.'''

        self.db = Database('db.json')
        self.user = User(self.db)
    


