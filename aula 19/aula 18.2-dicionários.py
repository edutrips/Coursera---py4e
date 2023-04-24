pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
for k in pessoas.keys(): #varre todas as keys de pessoas
    print(k)
for k, v in pessoas.items(): #varre todas as keys k para seu respectivo valor nos itens de pessoas
    print(f'{k} = {v}')
#dicionários dentro de listas:
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf']) #vai mostrar no elemento 0 (rio) a unidade federal(Rio de Janeiro)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for v in e.items():
        print(v, end ='')
    print()