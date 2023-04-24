pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 0
while not c >= 10:
    p = pt+c*r
    c+=1
    print('o {} termo é {}' .format(c,p))
termos = int(input('Você quer ver mais quantos termos? '))
if termos != 0:
    for c in range(c, termos+c):
        p = pt+c*r
        c+=1
        print('o {} termo é {}' .format(c,p))
print('Progressão finalizada com {} termos mostrados' .format(c))
print('Fim')
