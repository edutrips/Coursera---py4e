num = int(input('Digite um número inteiro qualquer: '))
base = int(input('''Escolha qual será a base de conversão: 
1 para binário
2 para octal
3 para hexadecimal ''' ))
if base == 1:
    print('{} convertido para binário é igual a {}' .format(num, bin(num)))
elif base == 2:
    print('{} convertido para octal é igual a {}' .format(num, oct(num)))
elif base == 3:
    print('{} convertido para hexadecimal é igual a {}' .format(num, hex(num)))
else:
    print('Opção inválida')