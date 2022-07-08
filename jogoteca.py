from crypt import methods
from flask import Flask, render_template, request, redirect, session, flash
#request fornece a função form para passar dados do formulario para o servidor 
#render_template trata-se de um Helper
#importando framework

class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        
jogo1 = Jogo('Tetriz Z','Puzzle','Atari')
jogo2 = Jogo('God Of War 2','Rack and Slash','PS2')
jogo3 = Jogo('Mortal Kombat','Luta','PS2')
lista = [jogo1, jogo2, jogo3]
        

app = Flask(__name__)
# __name__ faz uma referencia ao próprio arquivo em questão 
app.secret_key = 'avada'
#definindo a secret key

#para utilizar é necessário criar as rotas da web e uma função especificando sua ação
@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos = lista)

#criação da rota de cadastros de jogos
@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo') #variavel proxima recebe valor 'novo'
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods = ['POST', ])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logado com sucesso')
        proxima_pagina = request.form['proxima']
        return redirect("/{}".format(proxima_pagina))
    else:
        flash('usuario não logado')
        return redirect('/login')
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')

#para rodar a aplicação 
app.run(
    debug=True
)