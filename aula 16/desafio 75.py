num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'O número 9 apareceu {num.count(9)} vezes')
print(f'O número 3 foi digitado na posição {num.index(3)}')
for c in num:
    if c%2 == 0:
        print(f'{c} é um número par.')
