valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for v in range(0, 3):
        valores[c][v] = int(input(f'Digite um valor para [{c}] [{v}]: '))
for c in range(0, 3):
    for v in range(0, 3):
        print(f'{valores[c][v]:^5}', end='')
    print()
