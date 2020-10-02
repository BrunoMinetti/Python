# Linguagem de Programação II
# AC01 ADS-EaD - Números Especiais
#
# Email Impacta: Modelo fornecido por alissa.munerato@aluno.faculdadeimpacta.com.br


def eh_primo(n):
  if isinstance(n, int) == False:
    return print("apenas números naturais")
    
  prime_list = []
  for i in range(2,n):
    if n % i == 0:
      prime_list.append(i)
    if len(prime_list) > 0:
      return False
    else:
      return True
pass


def lista_primos(n):
    if isinstance(n, int) == False:
      return print("apenas números naturais")
    prime_list = []
    for i in range(2,n):
      if eh_primo(i):
        prime_list.append(i)
    return print(prime_list)
pass


def eh_armstrong(n):

    if isinstance(n, int) == False:
      return print("apenas números naturais")
    number_list = list(str(n))
    power_list = []
    for i in number_list:
      power_list.append(int(i)**len(number_list))
    
    sum_number_list = sum(power_list)
    
    if n == sum_number_list:
      return True
    else:
      return False
    
pass


def lista_armstrong(n):
    if isinstance(n, int) == False:
      return print("apenas números naturais")
    armstrong = []
    for i in range(1,n):
      if eh_armstrong(i):
        armstrong.append(i)
    return print(armstrong)
pass


def eh_perfeito(n):
    if isinstance(n, int) == False:
      return print("apenas números naturais")
    perfect_list = []
    for i in range(1,n):
      if n % i == 0:
        perfect_list.append(i)
    n2 = sum(perfect_list)
    if n == n2:
      return True
    else:
      return False
pass


def lista_perfeitos(n):
    if isinstance(n, int) == False:
      return print("apenas números naturais")
    perfeito = []
    for i in range(1,n):
      if eh_perfeito(i):
        perfeito.append(i)
    return print(perfeito)
pass
