v = int(input('Velocidade do carro: '))
multa = (7 * (v - 80))
if v > 80.0:
    print('Você estava a {} km/h e foi multado em {} reais' .format(v, multa))
