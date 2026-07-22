lista = []
def aleatory (a):
    import random
    a = input("\nDigite algo para ser randomizado: ").title()
    lista = list(a)
    random.shuffle (lista)
    return "".join(lista)
x = aleatory (lista)
print (x)


