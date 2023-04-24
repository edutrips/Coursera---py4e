menu = 0
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
while menu != 5:
    menu = int(input('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    '''))
    if menu == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}' .format(n1, n2, soma))
    if menu == 2:
        mult = n1*n2
        print('A multiplicação entre {} e {} é {}' .format(n1, n2, mult))
    if menu == 3:
        if n1 > n2:
            maior = n1
            menor = n2
            print('O maior é {} e o menor é {}' .format(n1, n2))
        elif n2 > n1:
            maior = n2
            menor = n1
            print('O maior é {} e o menor é {}' .format(n2, n1))
        else:
            print('Os dois são iguais')
    if menu == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
print('Fim')