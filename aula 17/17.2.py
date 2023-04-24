num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse = True)
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.remove(5)
print(num)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores): #mostra a posição c e o valor v da lista valores
    print(f'Na posição {c} encontrei o valor {v}...')
a = [2, 3, 4, 7]
b = a
b[2] = 8 #o python iguala as duas listas e as duas receberão o valor 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')