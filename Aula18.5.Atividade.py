import os

# os.getcwd()
# os.mkdir("Pasta Haxorus")
# os.chdir()
# os.listdir()
# os.remove("Arquivo.txt")

nome_pasta = input("Digite o nome da pasta: ")
if os.path.exists(nome_pasta):
    print("\nEssa pasta já existe ")
else:
    os.mkdir(nome_pasta)
    print("\nPasta criada com sucesso ")

nome_arquivo = input("Digite o nome do arquivo: ")

nome_arquivo += ".txt"

os.listdir(nome_pasta)

os.chdir(nome_pasta)

