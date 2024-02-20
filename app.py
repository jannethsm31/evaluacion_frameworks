import web


urls = (
    "/", "mvc.controllers.index.Login",
    "/bienvenida", "mvc.controllers.bienvenida.Bienvenida"
)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()