#estruturas condicionais
#if
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro tá novo')
else: 
    print('Seu carro tá véio')

#condição simplificada
tempo = int(input('Quantos anos tem seu carro? '))
print('Seu carro tá novo' if tempo<= 3 else 'Seu carro tá véio')
print('Fim')