from random import randint
jogos = int(input('Quantos jogos serão gerados? '))
jogo = []
palpites = [[], []]
for i in range(0, jogos):
    jogo.append(i)
    for c in range(0, 6):
        jogo.append(randint(1, 60))
    palpites[0].append(jogo[0])
    jogo.clear()
    print(palpites)
