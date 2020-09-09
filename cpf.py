import requests as Req

url = "https://www.4devs.com.br/ferramentas_online.php"

form = {'acao':'gerar_cpf','pontuacap':'s'}

cpf = Req.post(url, data = form).text

print(f"CFP gerado: {cpf}")
