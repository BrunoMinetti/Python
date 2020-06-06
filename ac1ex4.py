# ac1 ex4

# Imagine que você fora contratado para fazer um programa para uma loja de tintas, com o objetivo de calcular quantas latas de tinta são necessárias para pintar uma determinada área e calcular o preço final da compra.

# A loja trabalha com latas de tinta de:
# 24 litros, vendidas a R$91,00 cada e,
# 5.4 litros, vendidas a R$23,00 cada.
# Sabe-se ainda que cada litro de tinta cobre uma superfície de 7 metros quadrados.

# Faça um programa que receba o valor da área a ser pintada em metros quadrados, calcule e imprima:

# a) A quantidade de latas de tinta e o preço final, considerando apenas latas de 24 litros.
# b) A quantidade de latas de tinta e o preço final, considerando apenas latas de 5.4 litros.
# c) A quantidade de latas de tinta e o preço final, considerando ambas as latas, de 24 e 5.4 litros.

# Saida

# a) 2 lata(s) de 24 litros: R$ 182.00
# b) 6 lata(s) de 5.4 litros: R$ 138.00
# c) 1 lata(s) de 24 litros e 1 lata(s) de 5.4 litros: R$ 114.00

import math

areaTotal = float(input())

areaMin = 7 #area minima em m**2

prc24 = 91 #valor de uma lata de 24l
prc5_4 = 23 #valor de uma lata de 5.4l

volume = areaTotal / areaMin #volume de tinta necessária para pintar a area desejada

qtdLatas24 = math.ceil(volume / 24) #quantidade de latas de 24l necessarias para pintar a area desejada

qtdLatas5_4 = math.ceil(volume / 5.4) #quantidade de latas de 5.4l necessarias para pintar a area desejada

prcFinal24 = qtdLatas24 * prc24 #preco final utilizando latas de 24l

prcFinal5_4 = qtdLatas5_4 * prc5_4 #preco final utilizando latas de 5.4l

print(f'a) {qtdLatas24:.0f} lata(s) de 24 litros: R$ {prcFinal24:.2f}')
print(f'b) {qtdLatas5_4:.0f} lata(s) de 5.4 litros: R$ {prcFinal5_4:.2f}')

qtdMix24 = volume // 24 #quantidade mínima necessária de latas de 24l

qtdMix5_4 = math.ceil((volume % 24) / 5.4) #quantidade mínima necessária de latas de 5.4l

prcMixFinal = qtdMix24 * prc24 + qtdMix5_4 * prc5_4 #preco otimizado utilizando os dois volumes de tinta

print(f'c) {qtdMix24:.0f} lata(s) de 24 litros e {qtdMix5_4:.0f} lata(s) de 5.4 litros: R$ {prcMixFinal:.2f}')

