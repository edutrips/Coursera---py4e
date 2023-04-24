menor = ' '
total = produtos = cont = 0
while True:
    nome = str(input('Qual o nome do produto? '))
    preço = float(input('Qual o preço do produto? '))
    cont += 1
    if cont == 1:
        menorp = preço
    else: 
        if preço < menorp:
            menor = nome
    total += preço
    if preço > 1000.0:
        produtos += 1
    usuário = str(input('Quer continuar? ')).upper()[0] .strip()
    if usuário not in 'S':
        break
print(f'O total gasto na compra é {total}, {produtos} produtos custam mais de R$ 1000, e o produto mais barato é {menor}')
        
