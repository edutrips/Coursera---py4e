a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 1
b = 2
s = a + b
print(s)
#como repetir menos?
def soma(a, b):
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(2, 1)
#empacotamento: 
def contador(*núm): # o '*' diz que eu não sei quantos parâmetros serão passados
    print(núm)

def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos]*=2
        pos += 1
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)