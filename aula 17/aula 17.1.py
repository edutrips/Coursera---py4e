lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'picole'
#para adicionar um elemento à lista, basta usar o .append('elemento')
lanche.append('Cookie')
lanche.insert(0,'cachorro-quente')
#del lanche[3] #eliminar elementos da lista
#lanche.pop(3)#também serve para eliminar, mas normalmente é usado pra remover o último
#lanche.remove('pizza') #serve pra eliminar tbm
#melhor método pra usar o remove:
if 'pizza' in lanche:
    lanche.remove('pizza')
#criar listas com range:
valores = list(range(4,11))
#valores.sort() para ordenar os valores da lista
#valores.sort(reverse=True) para ordenar ao contrário
#len(valores) para contar a qtd de elementos
