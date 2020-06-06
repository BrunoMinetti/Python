x=int(input())
n=int(input())

c = 0
prod=0

while prod < n:
    c = c + 1
    prod = x * c

c=c-1
print('O numero {} tem {} multiplos menores que {}.'.format(x,c,n))
