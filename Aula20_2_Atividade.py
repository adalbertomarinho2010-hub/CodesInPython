class Animal:
    def __init__(self,nome,peso):
        self.nome = nome
        self.peso = peso

    def cor(self, coloracao):
        print ("A cor desse animal é", coloracao)

    def habitat(self, lugar):
        print ("O habitat desse animal é", lugar)

    def movimento(self, distancia):
         print ("A distância que esse animal percorre diariamente é", distancia,"km\n")

a1 = Animal("Urso",80)
a2 = Animal("Raposa",40)

print (a1.nome)
print (a1.peso)
a1.cor("Completamente marrom")
a1.habitat("Florestas")
a1.movimento(10)

print (a2.nome)
print (a2.peso)
a2.cor("Avermelhada com pintas")
a2.movimento(25)