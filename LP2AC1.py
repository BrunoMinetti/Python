# Linguagem de Programação II
# AC01 DP/ADAP - Números Especiais
#
# Email Impacta: nome.sobrenome@aluno.faculdadeimpacta.com.br
##### ATENÇÃO
# Implemente apenas o código das funções nesse arquivo,
# sem uso de input nem print
# para testar o seu código, crie outro arquivo na mesma pasta
# e faça a importação deste módulo.
# Exemplo de teste em outro arquvio:
# import numeros
#
# print(numeros.eh_primo(7))
#
# O comando acima deverá imprimir True no teste, pois 7 é primo
def eh_primo(n):
    """Função que recebe um número natural e retorna verdadeiro se
    n é um número primo e falso caso contrário
    Um número é dito primo se possuir apenas 2 divisores, isto é,
    não possuir nenhum divisor além do 1 e do próprio n
    Ex: 29 é primo:
    divisores de 29: 1, 29
    Ex: 30 NÃO é primo:
    divisores de 30: 1, 2, 3, 5, 6, 10, 15, 30
    Parameters
    ----------
    n : int
    Número natural a ser testado
    Returns
    -------
    bool
    True se n for um número primo e False caso contrário
    """
    soma = 0
    for cont in range(2,n):
        if (n % cont == 0):
            print ("Múltiplo de ", cont)
            soma +=1
    if (soma == 0):
        return "é Primo!"
    else:
        return "Tem ", soma, " múltiplos acima de 2 e abaixo de ", n
            


def lista_primos(n):
    """Função que recebe um número natural e retorna uma lista com
    todos o
    números primos estritamente menores que ele
    Parameters
    ----------
    n : int
    Número natural que define o limite superior da lista
    Returns
    -------
    List[int]
    Uma lista contendo todos os números primos menores que n
    """
pass
def eh_armstrong(n):
    """Função que recebe um número natural e retorna verdadeiro se
    n é um número de Armstrong e falso caso contrário
    Um número é dito número de Armstrong se a soma de seus digitos
    elevados ao número total de digitos é igual a ele próprio
    Ex: 153 é número de Armstrong:
    1 ** 3 + 5 **3 + 3 ** 3 = 1 + 125 + 27 = 153
    Ex: 4 é número de Armstrong:
    4 ** 1 = 4
    Parameters
    ----------
    n : int
    Número natural a ser testado
    Returns
    -------
    bool
    True se n for um número de Armstrong e False caso contrário
    """
    pass
def lista_armstrong(n):
    """Função que recebe um número natural e retorna uma lista com
    todos o
    números de Armstrong estritamente menores que ele
    Parameters
    ----------
    n : int
    Número natural que define o limite superior da lista
    Returns
    -------
    List[int]
    Uma lista contendo todos os números de Armstrong menores que n
    """
    pass
def eh_perfeito(n):
    """Função que recebe um número natural e retorna verdadeiro se
    n é um número perfeito e falso caso contrário
    Um número é dito perfeito se a soma de todos os divisores próprios
    é
    igual a ele mesmo.
    Ex: 6 é um número perfeito:
    divisores próprios de 6: 1, 2, 3
    1 + 2 + 3 = 6
    Ex: 12 NÃO é um número perfeito:
    divisores próprios de 12: 1, 2, 3, 4, 6
    1 + 2 + 3 + 4 + 6 = 16
    Parameters
    ----------
    n : int
    Número natural a ser testado
    Returns
    -------
    bool
    True se n for um número perfeito e False caso contrário
    """
    pass
def lista_perfeitos(n):
    """Função que recebe um número natural e retorna uma lista com
    todos os números perfeitos estritamente menores que ele
    Parameters
    ----------
    n : int
    Número natural que define o limite superior da lista
    Returns
    -------
    List[int]
    Uma lista contendo todos os números perfeitos menores que n
    """
    pass
