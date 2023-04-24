jogadores = dict()
partidas = list()
jogadores['nome'] = str(input('Nome: '))
jogadores['partidas'] = int(input('Quantidade de partidas: '))
for c in range(0, jogadores['partidas']):
    partidas.append(int(input(f'Quantidade de gols da partida {c+1}: ')))
jogadores['gols'] = partidas[:]
jogadores['total'] = sum(partidas)
print(f'O jogador {jogadores["nome"]} tem {jogadores["partidas"]} partidas.')
for i, v in enumerate(partidas):
    print(f'Na partida {i+1}, {jogadores["nome"]} fez {v} gols')
print(f'Total de {jogadores["total"]} gols')