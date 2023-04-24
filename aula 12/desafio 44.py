pnormal = int(input('Preço normal do produto: '))
condição = int(input('Digite 1 para à vista no dinheiro, 2 para à vista no cartão, 3 para em até 2x no cartão, e 4 para 3x no cartão ou mais'))
if condição == 1:
    preço = pnormal*0.9
    print('O preço ficará R${}' .format(preço))
elif condição == 2:
    preço = pnormal*0.95
    print('O preço ficará R${}' .format(preço))
elif condição == 3:
    print('O preço ficará R${}' .format(pnormal))
else:
    preço = pnormal*1.2
    print('O preço ficará R${}' .format(preço))