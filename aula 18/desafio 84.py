dados = list()
pessoas = list()
pesados = []
leves = []
while True:           #cadastro das pessoas
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])     #cópia dos dados para a lista pessoas
    dados.clear()
    ctn = str(input('Quer continuar? ')).upper()[0] .strip()
    if ctn in 'N':
        break
print(f'As pessoas cadastradas são: {pessoas}')
for c in pessoas:
    if c[1] > 75: 
        pesados.append(c[0])
    else:
        leves.append(c[0])
print(f'{len(pessoas)} pessoas foram cadastradas, as pessoas mais pesadas são {pesados} e as mais leves são {leves}')
