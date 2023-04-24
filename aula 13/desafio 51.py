pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
décimo = pt +(10-1)*r
for c in range(pt, décimo, r):
    print('{}' .format(c), end = ' ')
