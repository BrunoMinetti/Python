"""
Bancário. Escreva um programa que registre o caixa de um banco. O programa
começa perguntando se o usuário quer criar uma nova conta ou fechar o programa.
Se ele escolher fechar o programa escreve uma mensagem de agradecimento e fecha,
caso contrário ele vai pedir que o usuário swelecione um número com 6 digitos e,
então se o número não existir no registro do banco, ele irá pedir um valor de
depósito. Depois o banco pergunta se deseja ver o saldo, se sim ele vai imprimir
aula10e.py
"""

contas = []
depositos = []
saldo = 0

def main():
    opção = bool(int(input('Deseja criar conta (1) ou fechar o programa (0): ')))
    while opção:
        CriaConta()
        VerSaldo()
        opção = bool(int(input('Deseja criar conta (1) ou fechar o programa (0): ')))

def CriaConta():
    global contas, depositos, saldo
    num_conta = int(input('Digite um número de conta: '))
    while num_conta in contas:
        print('conta já existente. Digite novamente')
        num_conta = int(input('Digite um número de conta: '))

    contas.append(num_conta)

    deposito = float(input('Digite o valor do seu primeiro depósito: '))
    while deposito <=0:
        print('Valor de depósito inválido')
        deposito = float(input('Digite o valor do seu primeiro depósito: '))
    depositos.append(deposito)
    saldo += deposito

def VerSaldo ():
    global saldo
    opção = bool(int(input('Deseja ver o saldo do banco(1 - Sim e 0 - Não): ')))
    if opção:
        print('O saldo do banco é R$ ',saldo)

main()
    

    
