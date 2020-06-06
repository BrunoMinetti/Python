def fatorial(numero):
    resultado=1
    for n in range(1,numero+1):
        resultado*=n
    print(resultado)

def acronimo(palavra):
    palavra=palavra.upper()
    letras=palavra[0]
    for i in range(1,len(palavra)-1):
        if palavra[i] == ' ':
            letras += palavra[i+1]
    return letras

def divisores(num):
    lista=[]
    for i in range(1,num+1):
        if num % i == 0:
            lista.append(i)
    print (lista)
            
def fibonacci(limite):
    'retorna o menor número de fibonacci maior que limite'
    anterior = 1
    atual = 1
    while atual <= limite:
        anterior, atual = atual, anterior+atual
    return atual

def ola2():
    while True:
        nome = input('Qual é o seu nome? ')
        print('Prazer {}!'.format(nome))

def cidade():
    lst=[]

    cidade=input('Digite a cidade: ')

    while cidade != '#':

        lst.append(cidade)
        cidade=input('Digite a cidade: ')
    return lst

def cidades():
    lst=[]
    while True:
        cidade = input('Digite a cidade: ')
        if cidade == '':
            return lst
        lst.append(cidade)
def double(y):
    x = 2
    print(' x = {}, y = {} '.format(x,y))
    return x*y
