import urllib.request
import json

soma = list()
caracteres = list()
link = urllib.request.urlopen(input('Link: ')).read()
data = json.loads(link.decode())
tam = int(len(data['comments'])) #quantos comments tem
print(tam)
for i in range(tam):
    count = data['comments'][i]['count']
    soma.append(int(data['comments'][i]['count']))
print(sum(soma))
