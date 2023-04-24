classificação = ('Palmeiras', 'Internacional', 'Fluminense',
                'Corinthians', 'Flamengo', 'Athletico-PR',
                'Atlético-MG', 'Fortaleza', 'São Paulo',
                'América-MG', 'Botafogo', 'Santos', 
                'Goiás', 'Bragantino', 'Coritiba', 'Cuiába',
                'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')
print('Os cinco primeiros colocados são: ', end = '')
print(classificação[0:6])
print('Os quatro últimos colocados são: ', end = '')
print(classificação[-4:])
print(f'Os times em ordem alfabética são: {sorted(classificação)}')
print(f'O time da chapecoense não está entre os 20 primeiros colocados.')