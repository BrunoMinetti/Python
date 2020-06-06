# Escreva um programa em Python3 que receba quatro números reais (a, b, c, d) e reproduza as seguintes expressões algébricas:

import math

a = float(input())
b = float(input())
c = float(input())
d = float(input())


i = round(((a**2 + 3*b)/c + d),4)
print('i)',i)

ii = round((math.log10(a) + math.e**(-b/c)-(d**2/math.pi)),4)
print('ii)',ii)

iii = round(((((a**(2/3))*(b**(1/3)))+(c*d))/(a+b+c+d)),4)
print('iii)',iii)

iv = round((((a+b)*(c+d))/(a*b*c*d)),4)
print('iv)',iv)

v = round((((a**2+b**2)/(c*d))-((c**2+d**2)/(a*b))),4)
print('v)',v)

vi = round(((a+b+c+d)**2),4)
print('vi)',vi)

vii = round((a**2+b**2+c**2+d**2),4)
print('vii)',vii)

viii = round(((a*b*c*d)**(1/3)),4)
print('viii)',viii)
