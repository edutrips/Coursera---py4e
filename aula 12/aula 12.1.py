#if, elif, else
#if carro.esquerda():
 #bloco 1
#elif carro.direita():
 #bloco 2
 #elif carro.ré():
  #bloco 3
#else:
 #bloco 4

  
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}' .format(nome))