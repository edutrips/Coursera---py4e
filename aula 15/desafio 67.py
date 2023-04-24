n = int(input('Digite um número para ver a tabuada: '))
c = 1
while n > 0:
    for c in range(c, 11):
        print(f'{n} x {c} = {c*n}')
    c = 1
    n = int(input('Digite um número para ver a tabuada: '))
    if n <= 0:
        break
print('Fim')
