sexo = str(input('Digite o sexo: [M/F]')).strip().upper()[0]
while sexo not in 'mMfF':
    sexo = str(input('Inválido, digite novamente: ')).strip().upper()[0]
    print('{}' .format(sexo))
print('FIM')