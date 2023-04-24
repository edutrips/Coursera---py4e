import math
cop = float(input('Digite o cateto oposto: '))
cad = float(input('Digite o cateto adjacente: '))
h = math.hypot(cop, cad)
print('O comprimento da hipotenusa é {}' .format(h))