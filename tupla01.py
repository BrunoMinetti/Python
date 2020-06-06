contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quize', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numero = int(input('Digite um número de 0 a 20: '))

if numero <0 and numero >20:
    numero = int(input('Você digitou errado, tente novamente: '))

print(contagem[numero])