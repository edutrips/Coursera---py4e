#dicionários permitem colocar indices literais
#declaração: dados = dict()
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M' # adiciona o elemento no dicionário
del dados['idade'] #elimina o elemento idade e o seu valor
filme = {'titulo': 'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas'
} #esses elementos (titulo, ano e diretor) são chamados de keys
print(filme.values()) # valores são os que estão depois do : e são individuais 
print(filme.keys()) #as chaves são os nomes que eu dei para cada objeto (ano, titulo, diretor)
print(filme.items()) #os itens são o conjunto keys+values
for k, v in filme.items(): #dentro dos itens de filmes, para cada k existe um v respectivo
    print(f'o {k} é {v}')
