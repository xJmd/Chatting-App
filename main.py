from server import *

class App(BaseApp, User, Chat):
    def __init__(self):
        super().__init__(__name__)


    
    def pages(self):
        @self.app.route('/ping')
        def ping():
            return '1'
        
        self.login()
        self.signup()

        self.chat()
        
        # @self.app.route('/', methods=['GET', 'POST'])
        # def helloworld():
        #     req = request.json
        #     print('Request:', req)
        #     return '"Good stuff"'


if __name__ == '__main__':
    app = App()
    app.pages()
    app.run(debug=True)