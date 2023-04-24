import re
import urllib.request
from bs4 import BeautifulSoup
link = urllib.request.urlopen(input('Link: ')).read() #abre a url como se fosse um arquivo
soup = BeautifulSoup(link, 'html.parser')# é um objeto que converte toda a URL para html e a trasforma numa "sopa"
tags = soup('span') #me dá uma lista do html da URL que mostra todas as linhas de "span" que a página contém
soma = 0
count = 0
for tag in tags: #vê cada uma das linhas do span
    # Look at the parts of a tag
    nome = str(tag)#linha span
    num = re.findall("[0-9]+", nome)#mostra cada número do span
    for c in num:
        c = int(c)
        soma += c
        count += 1
print(count)
print(soma)