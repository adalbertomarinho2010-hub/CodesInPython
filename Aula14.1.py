def cadastro_destino(nome_destino, valor_passagem, quantidade_vagas):
    
    print("\n" + "="*40)
    print("   CADASTRO DE DESTINO TURÍSTICO    ")
    print("="*40)
    
    while True:
        nome_informado = input("\nNome do local da viagem: ").strip().title()

        if not nome_informado:
            print("\n*** Erro: O nome não pode ser vazio! ***")
            continue

        nomes_minusculos = [n.lower() for n in nome_destino]
        if nome_informado.lower() in nomes_minusculos:
            print(f"Erro de logística: O local de Viagem '{nome_informado}' já existe!")
            continue

        while True:
            try:
                valor = float (input("\nDigite o valor da passagem (R$): "))
                if valor <=0:
                    raise ValueError
                break
            except ValueError:
                print ("\n*** Erro! Digite um valor válido ***")
                continue

        while True:
            try:
                vagas = int (input("\nDigite a quantidade de vagas existentes: "))
                if vagas <= 0:
                    raise ValueError
                break
            except ValueError:
                print ("\n*** Erro! Digite um valor válido ***")
                continue
        
        nome_destino.append (nome_informado)
        valor_passagem.append (valor)
        quantidade_vagas.append (vagas)
        
        print (f"\nSucesso: '{nome_informado}' cadastrado com sucesso!")
        

        return nome_destino, valor_passagem, quantidade_vagas

def destinos_turisticos(lista_destinos_turisticos):

    print("\n" + "="*40)
    print("   LISTA DE DESTINOS TURÍSTICOS    ")
    print("="*40)

    while True:
        if len(nome_destino) == 0:
            print ("\nNenhum destino cadastrado ainda!")
            break
        for indice in range (len(nome_destino)):
            print (f"\n- Destinos disponíveis: {nome_destino[indice]} \n- Valor: {valor_passagem[indice]} \n- Quantidade de Vagas: {quantidade_vagas[indice]} ")
        

        return lista_destinos_turisticos
    
def comprar_passagem(quantidade_vagas, valor_arrecadado):

    print("\n" + "="*40)
    print("   COMPRA DE PASSAGENS    ")
    print("="*40)

    while True:
        nome_para_busca = (input("\nDigite o nome do local: ")).strip()
        for indice in range(len(nome_destino)):
            if nome_destino[indice].lower() == nome_para_busca.lower():
                print(f"\nNome do destino: {nome_destino[indice]}")
                print(f"Valor da passagem: {valor_passagem[indice]}")
                print(f"Quantidade vagas: {quantidade_vagas[indice]}")
                if quantidade_vagas [indice] == 0:
                    print ("\nQuantidade de vagas esgotadas!")
                    break
                while True:
                    escolha_passagem = (input("\nVocê deseja comprar essa passagem?\n1 - Sim\n2 - Não\nDigite sua escolha: ")).strip()
                    if escolha_passagem == "1":
                        quantidade_vagas [indice ] = quantidade_vagas [indice] - 1
                        print (f"\nParabéns! Você comprou com sucesso uma passagem para '{nome_destino[indice]}'")
                        break
                    elif escolha_passagem == "2":
                        break
                    else:
                        print ("Digite uma escolha válida!")
                        continue
                break
            else:
                print("Local não encontrado.")

        return quantidade_vagas, valor_arrecadado
    
def vagas_restantes(quantidade_vagas):

    print("\n" + "="*40)
    print("   CONSULTAR VAGAS RESTANTES    ")
    print("="*40)

    while True:
        nome_para_busca = (input("\nDigite o nome do local: ")).strip()
        for indice in range(len(nome_destino)):
            if nome_destino[indice].lower() == nome_para_busca.lower():
                print(f"\nNome do destino: {nome_destino[indice]}")
                print(f"Valor da passagem: {valor_passagem[indice]}")
                print(f"Quantidade vagas: {quantidade_vagas[indice]}")
                print (f"\nQuantidade de vagas restantes: {quantidade_vagas[indice]}")
                break
            else:
                print("Local não encontrado.")

        return quantidade_vagas 

    

lista_destinos_turisticos = []
nome_destino = []
valor_passagem = []
quantidade_vagas = []
valor_arrecadado = []

while True:
    print("\n" + "="*60)
    print("     SISTEMA DE AGÊNCIA DE VIAGENS     ")
    print("="*60)
    print("1 - Cadastrar destino turístico")
    print("2 - Listar destinos disponiveis")
    print("3 - Comprar passagem")
    print("4 - Consultar vagas restantes")
    print("5 - Encerrar sistema")
    print("="*60)
    opcao = (input("\n Escolha a opção desejada: ")).strip ()

    match opcao:
        case "1":
            nome_destino, valor_passagem, quantidade_vagas = cadastro_destino(nome_destino, valor_passagem, quantidade_vagas)
        case "2":
            lista_destinos_turisticos = destinos_turisticos(lista_destinos_turisticos)
        case "3":
            quantidade_vagas, valor_arrecadado = comprar_passagem(quantidade_vagas, valor_arrecadado)
        case "4":
            quantidade_vagas = vagas_restantes(quantidade_vagas)