# def soma (x,y,z):
#     result = x + y + z
#     return result
# while True:
#     try:
#         a = int (input("\nPrimeiro número: "))
#         b = int (input("\nSegundo número: "))
#         c = int (input("\nTerceiro número: "))
#     except ValueError:
#         print ("\n** Digite apenas números! **")
#         continue
        
#     break
# res = soma(a,b,c)
# print ("\nSoma:",res)

# def somaImposto (taxaImposto, custo):
#     taxa = custo*(taxaImposto/100)
#     return custo + taxa

# def leitor (mensagem):
#     while True:
#         try:
#             a = int (input(mensagem))
#             break
#         except ValueError:
#             print ("\n** Digite apenas números! **")
#             continue
#     return a

# custo = leitor("Digite o custo: ")
# taxaImposto = leitor("\nDigite a taxa do imposto (%): ")
# total = somaImposto(taxaImposto,custo)
# print (total)

# def calculo_fuso(am,pm):
#     conversao = (am) - 12
#     return conversao

# def leitor (mensagem):
#     While True:
#         try:
#             a = int (input(mensagem))
#             break
#         except    