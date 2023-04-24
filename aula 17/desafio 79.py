valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
    else:
        while n in valores:
            n = int(input('O valor já existe na lista, digite outro: '))
    continuar = str(input('Quer continuar? ')).upper()[0] .strip()
    if continuar in 'N':
        break
print(sorted(valores))