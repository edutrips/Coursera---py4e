#interactive help
# dosctring
# argumentos opcionais
# escopo de variáveis
# retorno de resultados 
#interactive help: help() é uma função interna, ex:
#docstrings: """""" manual da função """"""
def contador(i,f,p):
    """
    -> faz uma contagem e mostra na tela.
    :param. i: inicio da contagem
    :param. f: fim da contagem
    :param. p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'c', end='..')
        c += p
    print('FIM')
contador(2, 10, 2)
help(contador)
#parâmetros opicionais, ex:
def somar(a, b, c=0): #esse é o parâmetro opcional
    s = a+b+c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)
