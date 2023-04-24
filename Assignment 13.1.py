import xml.etree.ElementTree as ET 
import urllib.request, urllib.parse, urllib.error

soma = list()
caracteres = list()
link = urllib.request.urlopen(input('Link: ')).read()
data = link.decode() #decodifica o XML e transforma em string
for letters in data:
    caracteres.append(letters)
tree = ET.fromstring(data) #transforma a string obtida em data em uma lista com árvores de XML
lista = tree.findall('comments/comment')
for item in lista:
    soma.append(int(item.find('count').text))

print(f'Retrieving {len(caracteres)}')
print(f'Count: {len(soma)}')
print(f'Sum: {sum(soma)}')