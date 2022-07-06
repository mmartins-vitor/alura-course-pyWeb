from flask import Flask, render_template
#render_template trata-se de um Helper
#importando framework

app = Flask(__name__)
# __name__ faz uma referencia ao próprio arquivo em questão 

#para utilizar é necessário criar as rotas da web e uma função especificando sua ação
@app.route('/init')
def hello():
    return render_template('lista.html')

#para rodar a aplicação 
app.run()