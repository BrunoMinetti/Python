p1 = float(input())
p2 = float(input())
p3 = float(input())
f = float(input())

media = round((2*p1+2*p2+3*p3)/7,1)
freq = f*100

print(f'Frequencia: {freq:.0f}%')
print(f'Media: {media}')

if freq < 75:
    print('Aluno reprovado por faltas!')
elif media > 9:
    print('Aluno aprovado com louvor!')
elif media >= 6:
    print('Aluno aprovado!')
elif media >= 4:
    print('Aluno de recuperação!')
else:
    print('Aluno reprovado!')
