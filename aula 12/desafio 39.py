ano = int(input('Qual seu ano de nascimento? '))
if (2023-ano) < 18:
    print('Ainda vai se alistar, você ainda tem {}' .format((2023-ano)))
elif (2023-ano) == 18:
    print('Já é hora de se alistar')
else:
    print('Passou do tempo de alistamento')