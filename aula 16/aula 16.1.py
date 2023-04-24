#tuplas (variáveis compostas)
'''lanche = hamburguer
lanche = suco''' #só tem espaço pra um dos lanches
# 3 tipos de variáveis compostas: tuplas, listas, dicionários
# os elementos são identificados por índices ([0,1,2,3..etc])
#os elementos das tuplas são acessados também por índices
print(lanche[2])
print(lanche[0:2])#só conta o 0 e o 1
print(lanche[1:]) #começa no 1 e vai até o final
print(lanche[-1]) #mostra o último elemento
len(lanche) #mostra quantos elementos tem lanche
for c in lanche:
    print(c)
#as tuplas são imutáveis: não posso mudar os elementos
