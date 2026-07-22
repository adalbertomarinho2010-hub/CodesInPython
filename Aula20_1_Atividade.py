class Pessoa:
    def __init__(self, altura, nome):
        self.altura = altura
        self.nome = nome

    def andar(self, passos):
        print ("Estou andando", passos, "passos")

    def respirar(self, respiracao):
        print ("Estou respirando", respiracao, "vezes")

    def somar(self, valor1, valor2):
        valor_final = valor1 + valor2
        print ("O valor somado é:", valor_final)

    def subtrair(self, valor1, valor2):
        valor_final = valor1 - valor2
        print ("O valor subtraido é:", valor_final, "\n")


p1 = Pessoa(1.85,"Greninja")
p2 = Pessoa(1.75,"Gardevoir")

print (p1.altura)
print (p1.nome)
p1.andar(200)
p1.respirar(100)
p1.somar(1,2)
p1.subtrair(10,2)

print (p2.altura)
print (p2.nome)
p2.andar(1000)
p2.respirar(200)
p2.somar(2,2)
p1.subtrair(8,4)