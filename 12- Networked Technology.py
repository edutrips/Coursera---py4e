#TCP - transport control protocol
#coneção entre o programa e o site
#TCIP PORTS: especificamente onde as aplicações entram
#web port: 80 HTTPS
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )#data é o host e 80 é o port


#Hypertext transfer protocol (HTTP)
#HTTP é a aplicação dominante na internet
#protocolo? é uma série de regras que temos que seguir para trabalhar
#http://www.dr-chuck.com/pagel.htm 
#protocol    #host       # document
#request de um documento: #GET (URL)

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'. encode() # o encode converte para UTF-8 bytes 
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())#decode converte de volta para o unicode( a linguagem que usamos)
mysock.close()
#12.3 Unicode Characters and strings
#ASCII código das cores
print(ord('H')) #mostra o número que o computador guarda da string H
print(ord('e'))
#em python 3, todas as strings são UTF-8
#12.4 Retrieving Web Pages
#existe uma biblioteca(urllib) que faz o trabalho do socket
#ela faz uma página da web ser lida como um arquivo
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')# é quase um open() de arquivo
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
#12.5 Parsing Web pages
#beautifulsoup
from bs4 import BeautifulSoup
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')# a biblioteca transforma a página em HTML em um objeto organizado
#anchortag é uma linha de código onde tem um link
tags = soup('a') #cria uma lista com os anchor tags da página de 'soup'
for tag in tags:
    print(tag.get('href', None))
