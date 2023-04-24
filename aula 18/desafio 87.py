valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = 0
soma3 = 0
for c in range(0, 3):
    for v in range(0, 3):
        valores[c][v] = int(input(f'Digite um valor para [{c}] [{v}]: '))
        if valores[c][v] % 2 == 0:
            somap += valores[c][v]
        if v == 2:
            soma3 += valores[c][v]
        if c == 1 and v == 0:
            maior = valores[c][v]
        elif c == 1 and valores[c][v] > maior:
            maior = valores[c][v]
for c in range(0, 3):
    for v in range(0, 3):
        print(f'{valores[c][v]:^5}', end='')
    print()
print(f'A soma de todos os valores pares digitados é {somap}, a soma dos valores da terceira coluna é {soma3} e o maior valor da segunda linha é {maior}')
