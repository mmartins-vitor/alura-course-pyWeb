from flask import Flask, render_template
#render_template trata-se de um Helper
#importando framework

class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        

app = Flask(__name__)
# __name__ faz uma referencia ao próprio arquivo em questão 

#para utilizar é necessário criar as rotas da web e uma função especificando sua ação
@app.route('/init')
def hello():
    jogo1 = Jogo('Tetris','Puzzle','Atari')
    jogo2 = Jogo('God Of War 2','Rack and Slash','PS2')
    jogo3 = Jogo('Mortal Kombat','Luta','PS2')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo = 'Jogos', jogos = lista)

#para rodar a aplicação 
app.run()