#Cria a função
def media(n):
    print(sum(n)/len(n))

#Carrega as notas
notas = []
for x in range (15):
    notas.append(float(input('digite a nota: ')))

#Chama função passando a lista por parâmetro
media(notas)
