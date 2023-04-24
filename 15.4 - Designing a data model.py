#15.4 - Designing a data model
#como os dados serão armazenados no banco de dados?
#tabelas, colunas, e conexões
#como conectar as tabelas?
#15.5 - Representing a data model in tables
#para conseguir conectar uma parte da tabela à outra, é necessário criar um ID (primary key)

#15.6 - Inserting Relational Data

#15.7 - Reconstructing Data with JOIN
#JOIN Operation 
#preciso dizer ao JOIN como usar as chaves para conectar as tabelas usando o ON
# select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id
#quero ver: Album.title, Artist.name #as tabelas que guardarão os dados: Album, Artist #como as tabelas serão ligadas: Album.artist_id=Artist.id
