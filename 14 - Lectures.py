#14.2 - Our first class and object
class PartyAnimal: #PartyAnimal é um template para fazer objetos
    x = 0

    def party(self):
        print(self.x)
        self.x += 1
        print("So far", self.x)
        
an = PartyAnimal() #constrói um objeto de PartyAnimal e armazena-o em uma variável
an.party() # é a mesma coisa de PartyAnimal.party(an)
an.party()
an.party()

#14.3 - Object Life Cycle
class PartyAnimal1:
    x = 0
    name = ""
    def __init__(self, z): #z é um parâmetro adicional, ele está relacionado com a "" da classe PartyAnimal(str)
        self.name = z
        print(self.name,'constructed')
    def party(self):
        self.x += 1
        print(self.name, 'party count', self.x)
s = PartyAnimal1("Sally") #Sally é um parâmetro
s.party()

j = PartyAnimal1("Jim")#jim é um parâmetro
j.party()#são duas coisas diferentes
s.party()  
print('-' *20)
#14.4 - Object Inheritance
#Quando fazemos uma nova classe, podemos reutilizar uma classe existente
#e HERDAR todas as suas habilidades (inherit)
#também pode ser chamada de subclasse
class FootballFan(PartyAnimal1):
    points = 0
    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points", self.points)  #esse bloco inteiro é uma extensao da classe PartyAnimal1
s = PartyAnimal1("Sally")
s.party()
j = FootballFan("Jim")
j.party()#chamo a função party e passo o parâmetro jim 
j.touchdown()
