estoque_loja = {
    "Camisetas": 50,
    "Bermuda": 25,
    "Nonés": 100
}

produto = input("Digite o produto desejado: ")
if produto in estoque_loja:
    print(f"{produto} está em estoque com {estoque_loja[produto]} unidades disponíveis.")
else:
    print(f"{produto} não está disponível no estoque.")
