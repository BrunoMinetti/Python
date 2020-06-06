numero = int(input())
multiplicador = 0
produto = 0

while (multiplicador<9):
    multiplicador += 1
    produto = numero * multiplicador
    print(f'{numero} X {multiplicador} = {produto}')
