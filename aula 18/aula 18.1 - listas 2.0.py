#relembrando
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) #pedro
print(dados[1]) #25
pessoas = list()
pessoas.append(dados[:]) #uma cópia dos dados dentro de pessoas
#pessoas é na verdade uma estrutura que guarda, até o momento, dois elementos de dados
#, no caso pedro e 25, e posso guardar por exemplo,'Maria' 19, 'João' 32 e assim por diante.
#outra forma de declarar:
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]] #são 3 listas, no caso, são listas dentro de listas
print (pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])