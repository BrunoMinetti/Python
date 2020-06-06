import json

# lista em JSON:
x = '{ "nome":"João", "idade":30, "cidade":"São Paulo"}'

# convertendo:
y = json.loads(x)

# o resultado é um dicionário em Python
print(y)

