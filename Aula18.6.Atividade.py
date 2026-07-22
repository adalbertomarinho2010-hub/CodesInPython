import pandas as pd

# dados = {
#     "Nomes": ["Gengar","Garchomp","Greninja"],
#     "Idade": [1,3,5],
#     "Profissão": ["Dealer","Tank","Speed"]
# }

# tabela = pd.DataFrame(dados)
# print(tabela)

# media = tabela["Idade"].mean()
# print(f"\n A média de Idade é: ", (media))

dados = {
    "Aluno": ["Gengar","Garchomp","Greninja"],
    "Nota 1": [1,3,5],
    "Nota 2": [7,8,9],
}

tabela = pd.DataFrame (dados)
print (tabela)

media1 = tabela["Nota 1"].mean()
media2 = tabela["Nota 2"].mean()
media_final = media1 + media2 / 2 
print (f"\n A média final é: {media_final}")