def h(n):
    print ('Inicia h')
    print(1/n)
    print(n)

def g(n):
    print('Inicia g')
    h(n-1)
    print(n)

def f(n):
    print('Inicia f')
    g(n-1)
    print(n)
