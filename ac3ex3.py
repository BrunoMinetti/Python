n=int(input())

lst=[]

for i in range(1,n+1):
    x=1/(i**2)
    lst.append(x)

soma=0

for i in range(len(lst)):
    soma=soma+lst[i]


print( '{:.6f}'.format(soma))
    
