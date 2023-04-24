peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
IMC = peso / (altura**2)
if IMC < 18.5:
    print('seu IMC é de {}, abaixo do peso' .format(IMC))
elif IMC >= 18.5 and IMC <=  24.9:
    print('seu IMC é de {}, peso ideal' .format(IMC))
elif IMC >= 25 and IMC <= 29.9:
    print('seu IMC é de {}, sobrepeso' .format(IMC))
elif IMC >= 30 and IMC <= 40:
     print('seu IMC é de {}, obesidade' .format(IMC))
else:
     print('seu IMC é de {}, obesidade mórbida' .format(IMC))
