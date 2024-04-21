from app import app
from flask import render_template

@app.route('/')
@app.route('/index', defaults={"nome":"User"})
@app.route('/index/<nome>/<profissao>/<idade>')
def index(nome, profissao, idade):
    dados = {"profissao": profissao, "idade": idade}
    return render_template('index.html', nome=nome, dados=dados)


@app.route('/contato')
def contato():
    return render_template('contato.html')