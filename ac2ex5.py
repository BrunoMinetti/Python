Salario = float(input())
DescINSS = 0

Teto = 5839.45

if Salario >= Teto:
    DescINSS = Teto * 0.11
elif Salario > 2919.72:
    DescINSS = Salario * 0.11
elif Salario > 1751.81:
     DescINSS = Salario * 0.09
else:
    DescINSS = Salario * 0.08

print(f'Desconto do INSS: R$ {DescINSS:.2f}')
