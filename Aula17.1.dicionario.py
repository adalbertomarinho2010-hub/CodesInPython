# tradutor = {}
# tradutor ["pineapple"] = "abacaxi"
# tradutor ["apple"] = "maça"
# tradutor ["orange"] = "laranja"
# print (type(tradutor))
# print (tradutor)

# tradutor1 = {}
# tradutor1 = {"Maçã" : "Apple", "Laranja" : "Orange", "Abacaxi" : "Pineapple"}
# print (type(tradutor1))
# print (tradutor1)

# tradutor2 = {}
# tradutor2 = {"Maçã" : "Apple", "Laranja" : "Orange", "Abacaxi" : "Pineapple"}
# print (tradutor1["Maçã"])

# tradutor3 = {}
# tradutor3 = {"Maçã" : "Apple", "Laranja" : "Orange", "Abacaxi" : "Pineapple"}
# print (tradutor3)
# del (tradutor3["Maçã"])
# print (tradutor3)
# print (tradutor3.pop("banana","fruta não encontrada"))///apaga o elemento se ele existir, caso não exista a segunda mensagem dps da virgula será exibida para não quebrar o código
# tradutor3.clear() /// limpa o conteúdo dentro da chave
# print (tradutor3)

# tradutor4 = {}
# tradutor4 = {"Maçã" : "Apple", "Laranja" : "Orange", "Abacaxi" : "Pineapple"}
# print ("Abacaxi" in tradutor4) /// o in retorna se o conteúdo digitado existe ou não (true ou false)

# tradutor5 = {}
# tradutor5 = {"Maçã" : "Apple", "Laranja" : "Orange", "Abacaxi" : "Pineapple"}
# print ("Apple" in tradutor5.values())/// retorna o valor 
# print (tradutor5.values())/// retorna o valor dentro do dicionário

# tradutor6 = {}
# tradutor6 = {"Maçã" : "Apple", "Laranja" : "Orange", "Abacaxi" : "Pineapple"}
# print (tradutor6)
# tradutor6 ["Apple"] = "Maçãzinha"/// "adiciona" mais um valor dentro do dicionário
# print (tradutor6)

# dados = {"Crossfox": {"Km":35000,"Ano":2025},"DS5": {"Km":45000,"Ano":2024},"Fusca": {"Km":130000,"Ano":1998},"Jetta":{"Km":95000,"Ano":2013}}
# print (dados)
# # um valor dentro da chave, recebe outro divionário dentro dele, sendo possivel criar um dicionário dentro do outro
# print (dados.get("Gol","Veículo não encontrado"))/// o ".get" serve para pegar as informações dentro de uma chave específica,caso não exista a segunda mensagem dps da virgula será exibida para não quebrar o código
# print (dados.get("Jetta"))

# mydict = {"cat":12,"dog":6,"elephant":23,"bear":20}
# print (mydict.keys()) /// O método "keys()" retorna uma visão contendo todas as chaves dentro do dicionário

# aluno = {
# "Nome": "Maria",
# "Idade": 18,
# "Curso": "Ads"
# }

# print (aluno.items()) # Mostra os elementos do dicionário na forma de pares (chave, valor)

# aluno = {
# "Nome": "Maria",
# "Idade": 18,
# "Curso": "Ads"
# }

# for aluno, Nome in aluno.items():
#     print(aluno,"->",Nome) #Usado para percorrer o dicionário

