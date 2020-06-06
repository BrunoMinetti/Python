import request

Retorno = request.get("http://www.impacta.edu.br")

print (Retorno.content)
