pessoasd = {}
pessoasl = []
soma = média = 0
while True:
    pessoasd['nome'] = str(input('Nome: '))
    pessoasd['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
    if pessoasd['sexo'] not in 'MF':
        pessoasd['sexo'] = str(input('Inválido, tente novamente: [M/F]'))
    elif pessoasd['sexo'] == 'F':
        pessoasd['mulheres'] = pessoasd['nome']
    pessoasd['idade'] = int(input('Idade: '))
    soma += pessoasd['idade']
    pessoasl.append(pessoasd.copy())
    continuar = str(input('Quer continuar? ')).upper()[0] 
    if continuar in 'N':
        break
print(f'{len(pessoasl)} pessoas foram cadastradas')
média = soma/(len(pessoasl))
print(f'A média de idade do grupo é de {média}')
print('As mulheres cadastradas foram: ', end='')
for c in pessoasl:
    if c['sexo'] in 'Ff':
        print(f'{c["nome"]}')
print('As pessoas com idade acima da média são: ', end ='')
for p in pessoasl:
    if p['idade'] > média:
        print(f'{p["nome"]} com {p["idade"]} anos. ')