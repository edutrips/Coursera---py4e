from random import randint
from time import sleep
numero = int(input('Descubra qual número o computador pensou: '))
aleatorio = randint(0, 5)
print('Processando...')
sleep(3)
if aleatorio == numero:
    print('Parabéns, você acertou')
else:
    print('O computador venceu')
    print('O computador pensou em {}' .format(aleatorio))