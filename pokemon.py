from requests import api
try:
    pokemon = int(input("Entre com o código do seu pokemon: (1-239): "))
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}#"
    ret = api.get(url)
    dic = ret.json()
    print("Seu pokemon é o "+dic["name"])
except ValueError:
    print("Você entrou com um código errado!")
