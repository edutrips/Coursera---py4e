numeros = []
cont = 0
while True:
    numeros.append(int(input('Digite um número: ')))
    continuar = str(input('Você quer continuar? ')).upper()[0] .strip()
    if continuar in 'N':
        break
print(f'Foram digitados {len(numeros)} numeros na lista')
numeros.sort(reverse=True)
print(f'Lista ordenada: {numeros}')
if 5 in numeros:
    print('O número 5 foi digitado')
else:
    print('O número 5 não foi digitado')
