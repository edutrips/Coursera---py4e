#a função open() serve para abrir um arquivo
#é usado como arquivo = open(filename, modo(read, write, etc))
#exemplo: fhand = open('mbox.txt', 'r')
fhand = open('mbox.txt', 'r')
print(fhand)
#newline: \n para pular uma linha
#é encontrado no fim de cada linha do arquivo aberto
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])
#ou
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() #tirar as linhas sem nada
    if line.startswith('From: '):
        print(line)
        
