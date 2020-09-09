import requests as Req

url = "https://api.github.com/events"

recurso = Req.get(url).json()

tipoEvento = recurso[0]['type']
usuario = recurso[0]['actor']['login']
repo = recurso[0]['repo']['name']

print(f"Usuário: {usuario}, tipo de evento: {tipoEvento}, repositório {repo}")

response = Req.get("https://api.github.com")

print(response.status_code)

#print(response.content)

#print(response.text)

#response.encding = "url-8"

#print(response.json())

#print(response.headers)

response = Req.get(url, params = {'nome' : 'valor'})

print(response.json())

r = Req.get(url, headers = {'Accept' : 'application/json'})

print(r.headers)
