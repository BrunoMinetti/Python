sentenca = str(input())
caractere= str(input())
contador = 0

for letra in sentenca:
    ch = letra
    if ch == caractere:
        contador +=1

if contador ==0:
    print('Caractere nao encontrado.')
else:
    print(f'O caractere buscado ocorre {contador} vezes na sequencia.')
