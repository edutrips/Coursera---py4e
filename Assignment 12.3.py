import urllib.request, re
from bs4 import BeautifulSoup

link = input('Link:')
position = int(input('Position:'))
count = int(input('Count: '))
link = urllib.request.urlopen(link).read() #abre o link e lê como se fosse um arquivo
soup = BeautifulSoup(link,"html.parser") #transforma o arquivo html em uma árvore de informações organizada com uma melhor visualização
href = soup('a') #é uma lista que guarda todos os arquivos que servem como anchor tags
for i in range(count):
    link = href[position-1].get('href', None) 
    print(href[position-1].contents[0]) #retorna a tag de href, nesse caso, o nome
    link = urllib.request.urlopen(link).read()#abre o link de novo
    soup = BeautifulSoup(link,"html.parser")
    href = soup('a')
    