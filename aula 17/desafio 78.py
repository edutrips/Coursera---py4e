valores = []
pos = []
for v in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if v == 0:
        maior = valores[v]
        menor = valores[v] 
    else:
        if valores[v] > maior:
            maior = valores[v]
            
        if valores[v] < menor:
            menor = valores[v]
print(f'O maior valor digitado foi {maior}, nas posições ', end ='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}.', end='')
print()
print(f' e o menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}.', end ='')
print()
