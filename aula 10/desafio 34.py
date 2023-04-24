salario = int(input('Digite seu salário: '))
if salario > 1250:
    aumento = salario*1.1
    print('O salário aumentará para {} reais' .format(aumento))
else:
    aumento = salario*1.15
    print('O salário aumentará para {} reais' .format(aumento))
    