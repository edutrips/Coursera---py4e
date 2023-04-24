alunos = []
aluno = []
cont = 0
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Primeira nota: ')))
    aluno.append(float(input('Segunda Nota: ')))
    alunos.append(aluno[:])
    cont += 1
    aluno.clear()
    ctn = str(input('Quer continuar? ')).upper()[0] .strip()
    if ctn in 'N':
        break
for c in range(0, cont):
    media = (alunos[c][1]+alunos[c][2])/2
    print(f'A média de {alunos[c][0]} foi {media}')
while True:
    consulta = str(input('Quer ver as notas individuais? ')).upper()[0] .strip()
    if consulta in 'N':
        break
    aluno.append(str(input('De qual aluno você quer ver as notas? '))).strip()
    print(f'As notas de {aluno} foram ', end ='')
    for c in range(0, 2):
        print(f'As notas de {aluno} foram {alunos[c][1], {alunos[c][2]}}')