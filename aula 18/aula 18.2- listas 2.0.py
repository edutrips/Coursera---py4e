teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # o : é para criar uma cópia, caso eu não fizer isso, as duas listas ficam iguais
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)