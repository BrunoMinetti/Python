#ac1 ex3
import math

Lado=float(input())

Area = 6*(Lado**2 * math.sqrt(3)) / 4
Perimetro = 6 * Lado

print(f'Lado do hexagono: {Lado} metros,')
print(f'Area: {Area} metros quadrados,')
print(f'Perimetro: {Perimetro} metros.')
