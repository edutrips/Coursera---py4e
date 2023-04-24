mais18 = 0
Hcad = 0
Mmenos20 = 0
while True:
    idade = int(input('Qual a idade da pessoa? '))
    if idade >= 18:
        mais18 += 1
    sexo = str(input('Qual o sexo da pessoa?[Masculino]/[Feminino] ')).upper()[0] .strip()
    if sexo == 'M':
        Hcad += 1
    if sexo == 'F' and idade < 20:
        Mmenos20 += 1
    usuário = str(input('Quer continuar? [Sim]/[Não]')).upper()[0] .strip()
    if usuário == 'N':
        break
print(f'O número de pessoas maiores de 18 é {mais18}, há {Hcad} homens cadastrados e há {Mmenos20} mulheres menores de 20 anos ')
