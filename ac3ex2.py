
r = int(input())
n = int(input())

a=1
lst=[1]
cont=1
while a < n:
    a=a+r
    
    lst.append(a)

soma=0
for i in range(len(lst)):
    soma=soma+lst[i]

print('A somatoria da PA eh: {}'.format(soma))
