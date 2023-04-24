aluno = dict()
aluno = {'nome': str(input('Nome: ')), 'média': float(input('Média: '))}
print(f' {aluno["nome"]} teve média {aluno["média"]} e foi ', end ='')

if aluno['média'] < 5:
    aluno['situação'] = 'reprovado'
else:
    aluno['situação'] = 'aprovado'
print(aluno['situação'])
for k, v in aluno.items():
    print(f'{k} é igual a {v}')