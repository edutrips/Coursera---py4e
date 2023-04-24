import urllib.request, urllib.parse, urllib.error
import json

key = input('Key: ')
link = 'http://py4e-data.dr-chuck.net/json?'
address = input('Enter Location: ')
while len(address) < 1:
    print('Retrieving: ', 'https://maps.googleapis.com/maps/api/geocode/json?}')
    address = input('Try Again: ')

atributos = {}
atributos['address'] = address
if key != 42:
    atributos['key'] = key
url = link + urllib.parse.urlencode(atributos)
print(f'Retrieving: {url}')
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print(f'Retrieved: {len(data)}')
info = json.loads(data)
print(info['results'][0]['place_id'])