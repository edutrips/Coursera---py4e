# ao invés de programar em linhas, programar com palavras
import re
x = 'My 2 favorite number are 19 and 42'
y = re.findall('[0-9]+', x)#mostra uma lista de strings 
print(y)
#re.search() #retorna True/False dependendo se encontrar a string
y = re.findall('[AEIOU]+', x)#verifica se em x existe alguma vogal em maiúsculo
print(y)
#Greedy matching, procura a maior string possível
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
#^ first character thats match
#.+ one or more characters
#: last character in the matchs
#non-Greedy matching
#^(Character).+?: 
x = 'From: Using the: character'
y = re.findall('^F.+?:', x)
print(y)
#como especificar mais a extração do .findall?
#usar parênteses! exemplo:
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', x)
print(y)
#como separar strings usando regular expressions?
words = x.split()
email = words[1]
pieces = email.split('@') #separa as palavras após essa string em duas partes
print(pieces[1])
#\S ou [^ ] significa um espaço em branco
y = re.findall('^From .*@([^ ]*)', x)
print(y)