email = 'bruno.sanches@aluno.faculdadeimpacta.com.br'
email1 = 'brunominetti@gmail.com'

def VerificaEmail(email):
    if email.split('@')[1] == 'aluno.faculdadeimpacta.com.br':
        return True
    else:
        return False

print(VerificaEmail(email))
print(VerificaEmail(email1))
