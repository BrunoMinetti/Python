from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/demo")
def hello():
    return "Olá mundo!"

if (__name__ == "__main__"):
    app.run()

@app.route('/alunos', methods = ['POST'])
def novo_aluno():
    novo_aluno = request.get_json()


@app.route('/alunos/<int:id_aluno>', methods = ['GET'])
def localiza_aluno(id_aluno):
    if id_aluno in database['ALUNO']: ...


@app.route('/alunos', methods = ['GET'])
def listar_alunos():
    inicio_nome = request.args.get('nome_inicia_com')
