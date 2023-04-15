from server.scripts import *

class App(BaseApp, Ping):
    def __init__(self):
        super().__init__(__name__)
    
    def pages(self):
        self.ping()


if __name__ == '__main__':
    app = App()
    app.pages()
    app.run(debug=True)