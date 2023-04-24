#API: application program interfaces
#mover dados entre programas e networks
#os  dois formatos mais usado são XML e JSON
#exemplo: python dictionary -> network -> JavaHashmap
#o dicionário em python sofre o método serialize em XML(network), e antes de passar para o javahashmap sofre de-serialize
#a serialização(serialization) envia um caracter por vez
#JSON é mais moderno que o XML
#13.2 - eXtensible Markup Language
#elementos em XML (ou nós):
#XML basics: https://prnt.sc/qMvNUzTKQJ4w
#XML as a Tree: https://prnt.sc/YGsRAkmawgmo
#13.4 - Parsing XML
import xml.etree.ElementTree as ET #chamo essa biblioteca de ET
#''' é um tipo de string
data = '''<person> 
    <name>Chuck</name>
    <phone type ='intl'>
    +1 734 303 4456
    </phone>
    <email hide = "yes"/>
   </person>'''
tree = ET.fromstring(data) #.fromstring pega a string e a transforma em uma árvore de XML
print('Name:', tree.find('name').text) #.find procura a tag name e .text escreve o que está na tag
print('Attr:', tree.find('email').get('hide'))#.find procura a tag email e .get confirma qual o atributo dela

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)#transforma a string ''' em uma árvore XML
lst = stuff.findall('users/user') #procura por users/user tags e os coloca em uma lista, ou seja, pega várias árvores e as coloca em uma lista
print('User count:', len(lst)) #mostra o tamanho da lista

for item in lst:
    print('Name', item.find('name').text)#mostra o nome
    print('Id', item.find('id').text)#mostra o id
    print('Attribute', item.get('x'))#mostra o atributo

#worked example
#13.5 JavaScript Object Notation(JSON)
import json
data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
  },
  "email" : {
      "hide" : "yes"
   }
}'''
info = json.loads(data)#é um objeto, que retorna um dicionário em python
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(input) #lista de dicionários
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
#13.6 - Service Oriented Approach
#13.7 - Using Application Programming Interfaces (API's)
#13.8 - Securing API Requests
'''import twurl
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print(data[:250])
    headers = dict(connection.getheaders())
    # print headers
    print('Remaining', headers['x-rate-limit-remaining'])
    
    

    
       
    # https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])
'''