def escreva(msg):
    tam = len(msg)
    print(f'-'*tam)
    print(msg)
    print(f'-'*tam)

escreva(str(input('Digite um texto: ')))