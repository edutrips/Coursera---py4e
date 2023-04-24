def contador(i, f, p):
    for c in range(1, 10):
        print(c)
    for c in range(10, 0, -2):
        print(c)
    for c in range(i, f, p):
        print(c)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)