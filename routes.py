from main import app

#rotas
@app.route("/")
def homepage():
    return "Meu site no Flask!"

@app.route("/blog")
def blog():
    return "Você está no blog."

@app.route("/celeste")
def celeste():
    return "Celeste é um jogo indie!!"