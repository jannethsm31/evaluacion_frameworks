# mvc/controllers/index.py
import web
from mvc.models.index import LoginIndex

render = web.template.render('mvc/views/')
login_index = LoginIndex()

class Login:
    def GET(self):
        return render.login(username='', password='')

    def POST(self):
        form = web.input()
        username = form.username
        password = int(form.password)  # Convertir la contraseña a un entero

        if login_index.validar_credenciales(username, password):
            web.setcookie('username', username)  # Guarda el nombre en una cookie
            raise web.seeother('/bienvenida')  # Redirige a la página de bienvenida
        else:
            return render.login(username=username, password='')
