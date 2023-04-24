from random import randint
cont = 0
while True:
    poi = ' '
    while poi not in 'PI':
        poi = str(input('Par ou impar? ')).strip() .upper()[0]
    pc = randint(0, 5)
    jogador = int(input('Digite o valor entre 0 e 5: '))
    while jogador > 5:
        jogador = int(input('Digite o valor entre 0 e 5: '))
    res = pc + jogador
    if poi == 'P':
        if res % 2 == 0:
            cont += 1
        else:
            print(f'Você jogou {jogador} e o pc jogou {pc}, total deu {res}, você perdeu')
            break
    if poi == 'I':
        if res % 2 != 0:
            cont += 1
        else:
            print(f'Você jogou {jogador} e o pc jogou {pc}, total deu {res}, você perdeu')
            break
print(f'Você teve {cont} vitórias consecutivas')