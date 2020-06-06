n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segunto número: '))

cont = n1
soma = 0
while cont < n2:
    soma = soma + cont
    cont = cont + 1
print('A soma dos valores é: ',soma)
