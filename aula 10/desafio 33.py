n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else: 
        menor = n2
    print('o maior é {} e o menor é {}' .format(n1))
if n2 > n1 and n2 > n3:
    maior = n2
    if n2 > n3:
        menor = n3
    else:
        menor = n2
if n3 > n1 and n3 > n2:
    maior = n3
    if n2 > n1:
        menor = n1
    else:
        menor = n2