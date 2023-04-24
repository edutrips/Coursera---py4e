
numeros = [[], []]

for c in range(1, 8):
    valores = int(input('Digite um valor: '))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
print(f'Os valores pares são {numeros[0]} e os ímpares são {numeros[1]}')
numeros.sort()
print(f'Os valores em ordem crescente são {numeros}')