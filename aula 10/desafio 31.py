d = int(input('Digite a distância da viagem em km: '))
if d <= 200:
    preço = d*0.5
    print('O preço da viagem é {} reais' .format(preço))
else:
    preço = d*0.45
    print('O preço da viagem é {} reais' .format(preço))