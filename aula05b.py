Produto = 100

codigo = int(input(' Entre com o código: '))

if codigo == 1:
    Produto = Produto * 0.9
    print(f'o valor do produto é R$ {Produto:.2f}')
elif codigo == 2:
    Produto = Produto * 0.95
    print(f'o valor do produto é R$ {Produto:.2f}')
elif codigo == 3:
    print(f'o valor do produto é R$ {Produto/2:.2f} em duas vezes sem juros')
elif codigo == 4:
    Produto = Produto * 1.10
    print(f'o valor do produto é R$ {Produto/3:.2f} em três vezes')
          
