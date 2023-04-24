from random import randint
from time import sleep
aleatorio = randint(0, 10)
palpite = 0
numero = int(input('Chute um número de 0 a 10: '))
print('Processando...')
sleep(3)
while numero != aleatorio:
    palpite += 1
    numero = int(input('Você errou, tente novamente: '))
print('você acertou, o número de palpites foi: {}' .format(palpite))
