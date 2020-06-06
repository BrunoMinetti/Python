import math

d = int(input('entre com o diamentro da lata '))
h = int(input('entre com a altura da lata '))

r = d / 2

v = math.pi * h * r**2

print (f'o volume da lata é {v:.4f}')
