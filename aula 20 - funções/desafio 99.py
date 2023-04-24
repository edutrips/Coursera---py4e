maiorn = 0
def maior(*lst):
    if lst[0]:
        maiorn = lst[0]
        print(maiorn)
    for c in lst:
            if c > maiorn:
                maiorn = c

parâmetros = []
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    parâmetros.append(num)
maior(parâmetros)    
print(maiorn)