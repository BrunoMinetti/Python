email = 'brunominetti@gmail.com'

usuario, dominio = email.split('@')

print(email[:(email.index('@'))])
print(email[((email.index('@'))+1):(email.index('.'))])
      
print()
print(email.split('@')[0])
print((email.split('@')[1]).split('.')[0])

print()
print(usuario)
print(dominio)
