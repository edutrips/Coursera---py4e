from random import randint
numa = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
maior = c = 0
for c in numa:
    if maior < c:
        maior = c
    else:
        menor = c
    print(c)
print(f'O maior é {maior} e o menor é {menor}')