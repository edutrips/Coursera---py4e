valor = int(input('Qual o valor da casa? '))
salário = int(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos ele vai pagar? '))
prestação = valor/(anos*12)
if prestação >= (0.3*salário):
    print('Você não pode financiar a casa, pois a prestação de {} excede seu salário, que é de {}' .format(prestação, salário))
else: 
    print('Parabéns! Você pode financiar a casa! A prestação será de {}' .format(prestação))
