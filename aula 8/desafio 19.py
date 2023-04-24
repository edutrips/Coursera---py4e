import random
a1 = input('Nome a1: ')
a2 = input('Nome a2: ')
a3 = input('Nome a3: ')
a4 = input('Nome a4: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno sorteado foi {}' .format(escolhido))