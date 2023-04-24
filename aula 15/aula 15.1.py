'''cont = 1
while True:
    print(cont, '-> ', end = '')
    cont += 1
print('Acabou')'''
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break #comando que para o laço
    s += n
print(f'A soma vale {s}')
