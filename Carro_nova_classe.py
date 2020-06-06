class Carro:
    def __init__(self, m, a, c):
        self.modelo = m
        self.ano    = a
        self.cor    = c

brasilia = Carro('Brasilia', 1968, 'amarela')
fusca = Carro('Fusca', 1981, 'preto')

fusca.ano += 10   # observe que podemos acessar atributos de fusca
print(fusca.ano)
