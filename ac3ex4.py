n=int(input())

lstP=[]
lstI=[]


for i in range(1,n+1):
    if i % 2 ==0:
        x=1/(i)
        lstP.append(x)
    else:
        x=1/(i)
        lstI.append(x)
        


somaP=0
for i in range(len(lstP)):
    somaP=somaP+lstP[i]


somaI=0
for i in range(len(lstI)):
    somaI=somaI+lstI[i]

soma=somaP-somaI

print( '{:.6f}'.format(soma))
    
