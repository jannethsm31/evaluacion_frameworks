import web

render = web.template.render('mvc/views')

class Bienvenida:
    def GET(self):
        username = web.cookies().get('username')
        if username:
            return render.bienvenida(username)
        else:
            raise web.seeother('/')