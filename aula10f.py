"""
Escreva uma função que receba um inteiro m e outro n e com isso
constrói uma matriz mxn
"""

matriz = []
m = int(input('Digite o número de linhas da matriz: '))
n = int(input('Digite o número de colunas da matriz: '))

def ConstróiMatriz(m, n, matriz):
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            x = int(input('Digite o elemento %i%i da matriz: '%(i,j)))
            linha.append(x)

        matriz.append(linha)

ConstróiMatriz(m, n, matriz)

print(matriz)
    
