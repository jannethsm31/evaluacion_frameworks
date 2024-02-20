import web

class LoginIndex:
    def __init__(self):
        self.username = "usuario"
        self.password = 1234
        return 

    def validar_credenciales(self, username, password):
        return username == self.username and password == self.password
