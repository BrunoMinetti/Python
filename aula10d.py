X = 10

def incrementa():
    global X
    incremento = 5 #variável local
    X += incremento

incrementa()

print(X)
