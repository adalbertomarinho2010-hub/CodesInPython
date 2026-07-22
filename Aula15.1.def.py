# def hello (nome):
#     print ("\nSeja bem vindo!", nome)

# nome = input ("\nDigite o seu nome: ")
# hello (nome)

# def calcular_pagamento (qnt_horas, valor_hora):
#     horas = float (qnt_horas)
#     taxa = float (valor_hora)
#     if horas <= 40:
#         salario = horas*taxa
#     else:
#         h_excd = horas - 40
#         salario = 40*taxa+(h_excd*(1.5*taxa))
#     print (salario)

# def soma (x,y):
#     result = x + y
#     return result

# a = int (input("\nPrimeiro número: "))
# b = int (input("\nSegundo número: "))

# res = soma(a,b)
# print ("\nSoma: ",res)

# def inverte(nome, sobrenome):
#     nomeInverso = sobrenome+","+nome
#     return nomeInverso
# nome = input("\nNome: ")
# sobrenome = input("\nSobrenome: ")

# def par(x):
#     if (x%2) ==0:
#         return True
#     else:
#         return False
# while True:
#     num = int (input("\nInsira um número: "))
#     if par(num):
#         print ("\nÉ par")
#     else:
#         print ("\nÉ impar")

def cadastro():
    name = (input("\nDigite o seu nome: "))
    age = int (input("\nDigite a sua idade: "))
    return name, age

print ("\nIniciando cadastro...")
nome, idade = cadastro()
print ("\nCadastro realizado com sucesso!")
print ("\nSeu nome é",nome,"e você tem",idade,"anos de idade\n")
