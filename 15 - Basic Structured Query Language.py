#15.1 - Relational Databases
#SQL, é a linguagem para criar tabelas, pegar dados, inserir dados e excluir dados
#como nos comunicamos com o banco de dados usando python?
#qual o caminho entre a aplicação e o banco de dados?
#oracle

#15.2 - Using Databases
#fazer input de arquivos(networks, arquivos, etc)
#filtrar os dados com o python e adicioná-los à base de dados
# os outputs são colocados em outro programa(R, Excel, etc)
#modelo da base de dados(schema)
#sistemas de base de dados comuns: Oracle, MySql, SqlServer

#15.3 - Single table CRUD
#para criar uma tabela, usar o comando CREATE TABLE (nome da tabela)
#                                          (nome da coluna) (tipo de variável),
#                                          (nome da coluna) (tipo de variável))
#SQL: insert: a declaração de inserir uma linha numa tabela:
#INSERT INTO (nome da tabela)(1° coluna, 2° coluna) VALUES('informação para 1° coluna', 'informação para 2° coluna')
#SQL: delete: a declaração é:
#DELETE FROM (nome da tabela) WHERE email='informação que quero deletar'
#SQL: Update: permite um update do campo que você quer
#UPDATE (nome da tabela) SET (nome da coluna)=(novo valor) WHERE (nome da coluna)=(novo valor)
#Retornando registros: Select
#SELECT * FROM (nome da coluna) # (*=todas as colunas)
#SELECT * FROM (nome da coluna) WHERE email='csev@umich.edu'
import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite') #conecta o arquivo sql no python
cur = conn.cursor() #funciona como um handle

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()[1]
    email = pieces.split('@')
    org = email[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone() #extrai as informações das colunas
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
