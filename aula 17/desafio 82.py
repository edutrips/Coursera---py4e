valores = []
p =[]
i = []
c = 0
while True:
    valores.append(int(input('Digite um número: ')))
    if valores[c] % 2 == 0:
        p.insert(c, valores[c])
    else:
        i.insert(c, valores[c])
    c += 1
    continuar = str(input('Quer continuar? ')).upper()[0] .strip()
    if continuar in 'N':
        break
print(f'A lista digitada é {valores}, os pares são {p} e os ímpares são{i}')
