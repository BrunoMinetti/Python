numeroInicial = int(input())
while not numeroInicial in range (1,10):
    print('Insira um número inicial entre 1 e 9')
    numeroInicial = int(input())
numeroFinal = int(input())
while not numeroFinal in range (1,10):
    print('Insira um número final entre 1 e 9')
    numeroFinal = int(input())
if numeroInicial > numeroFinal:
    print('Nenhuma tabuada nesse intervalo')
else:
    while (numeroInicial<=numeroFinal):
        multiplicador = 0
        produto = 0
        while (multiplicador<9):
            multiplicador +=1
            produto = numeroInicial * multiplicador
            print(f'{numeroInicial} x {multiplicador} = {produto}')
        numeroInicial +=1
        print()
