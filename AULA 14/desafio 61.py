pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 0
while not c >= 10:
    p = pt+c*r
    c+=1
    print('o {} termo é {}' .format(c,p))