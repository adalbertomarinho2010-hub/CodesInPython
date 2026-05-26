lista_de_nomes = []
lista_de_cidades = []
lista_de_estados = []
lista_de_funcionarios = []
lista_de_clientes = []
lista_de_faturamentos = []
lista_de_pedidos_entregues = []
lista_de_pedidos_cancelados = []
lista_de_notas = []
lista_de_pratos = []

while True:
    print("\n" + "="*40)
    print("     SISTEMA DE GESTÃO DE RESTAURANTES     ")
    print("="*40)
    print("1 - Cadastrar restaurante")
    print("2 - Exibir relatório completo (Filtros)")
    print("3 - Buscar restaurante pelo nome")
    print("4 - Mostrar estatísticas gerais")
    print("5 - Atualizar dados de restaurante")
    print("6 - Remover restaurante")
    print("7 - Encerrar sistema")
    print("="*40)
    
    opcao_escolhida = input("Escolha a opção desejada: ").strip()
    
    if opcao_escolhida == "1":
        print("\n" + "="*40)
        print("   CADASTRO DE RESTAURANTE    ")
        print("="*40)

        nome_informado = input("\nNome do restaurante: ").strip().title()
        
        if nome_informado == "":
            print("\n*** Erro: O nome não pode ser vazio! ***")
            continue
            
        for nome_salvo in lista_de_nomes:
            if nome_salvo.lower() == nome_informado.lower():
                print(f"Erro de logística: O restaurante '{nome_informado}' já existe!")
                break
        else:
            lista_de_nomes.append(nome_informado)
            
            cidade_informada = input("Cidade: ").strip().title()
            lista_de_cidades.append(cidade_informada)
            
            estado_informado = input("Estado: ").strip().upper()
            lista_de_estados.append(estado_informado)
            
            while True:
                try:
                    quantidade_funcionarios = int(input("Quantidade de funcionários: "))
                    if quantidade_funcionarios < 0:
                        print("\n*** Erro! A quantidade não pode ser negativa. ***")
                        continue
                    lista_de_funcionarios.append(quantidade_funcionarios)
                    break
                except ValueError:
                    print("\n*** Erro! Digite um número inteiro válido. ***")
                    
            while True:
                try:
                    quantidade_clientes = int(input("Clientes atendidos no mês: "))
                    if quantidade_clientes < 0:
                        print("\n*** Erro! A quantidade não pode ser negativa. ***")
                        continue
                    lista_de_clientes.append(quantidade_clientes)
                    break
                except ValueError:
                    print("\n*** Erro! Digite um número inteiro válido. ***")
                    
            while True:
                try:
                    faturamento_mensal = float(input("Faturamento mensal (R$): "))
                    if faturamento_mensal < 0:
                        print("\n*** Erro! O faturamento não pode ser negativo. ***")
                        continue
                    lista_de_faturamentos.append(faturamento_mensal)
                    break
                except ValueError:
                    print("\n*** Erro! Digite um valor numérico válido. ***")
                    
            while True:
                try:
                    pedidos_entregues = int(input("Quantidade de pedidos entregues: "))
                    if pedidos_entregues < 0:
                        print("\n*** Erro! A quantidade não pode ser negativa. ***")
                        continue
                    lista_de_pedidos_entregues.append(pedidos_entregues)
                    break
                except ValueError:
                    print("\n*** Erro! Digite um número inteiro válido. ***")
                    
            while True:
                try:
                    pedidos_cancelados = int(input("Quantidade de pedidos cancelados: "))
                    if pedidos_cancelados < 0:
                        print("\n*** Erro! A quantidade não pode ser negativa. ***")
                        continue
                    lista_de_pedidos_cancelados.append(pedidos_cancelados)
                    break
                except ValueError:
                    print("\n*** Erro! Digite um número inteiro válido.***")
                    
            while True:
                try:
                    nota_media = float(input("Nota média dos clientes (0 a 10): "))
                    if nota_media < 0 or nota_media > 10:
                        print("\n*** Erro! A nota deve ser estritamente entre 0 e 10. ***")
                        continue
                    lista_de_notas.append(nota_media)
                    break
                except ValueError:
                    print("\n*** Erro! Digite uma nota numérica válida. ***")
                    
            while True:
                try:
                    quantidade_pratos = int(input("Quantidade de pratos no cardápio: "))
                    if quantidade_pratos < 0:
                        print("\n*** Erro! A quantidade não pode ser negativa. ***")
                        continue
                    lista_de_pratos.append(quantidade_pratos)
                    break
                except ValueError:
                    print("\n*** Erro! Digite um número inteiro válido. ")
                    
            print(f"Cadastro Feito: '{nome_informado}' cadastrado com sucesso!")

    elif opcao_escolhida == "2":
        print("\n" + "="*40)
        print("     RELATÓRIO COMPLETO E FILTROS    ")
        print("="*40)

        if len(lista_de_nomes) == 0:
            print("Nenhum restaurante cadastrado ainda.")
            continue
            
        print("\nRestaurantes com mais de 100 pratos no cardápio:")
        for indice in range(len(lista_de_nomes)):
            if lista_de_pratos[indice] > 100:
                print(f"- {lista_de_nomes[indice]} ({lista_de_pratos[indice]} pratos)")
                
        print("\nRestaurantes com nota média acima de 9:")
        for indice in range(len(lista_de_nomes)):
            if lista_de_notas[indice] > 9:
                print(f"- {lista_de_nomes[indice]} (Nota: {lista_de_notas[indice]})")
                
        print("\nRestaurantes com faturamento acima de R$ 100.000,00:")
        for indice in range(len(lista_de_nomes)):
            if lista_de_faturamentos[indice] > 100000:
                print(f"- {lista_de_nomes[indice]} (R$ {lista_de_faturamentos[indice]:.2f})")
                
        maior_quantidade_clientes = lista_de_clientes
        indice_do_maior = 0
        for indice in range(1, len(lista_de_nomes)):
            if lista_de_clientes[indice] > maior_quantidade_clientes:
                maior_quantidade_clientes = lista_de_clientes[indice]
                indice_do_maior = indice
        print(f"\nMaior quantidade de clientes atendidos: {lista_de_nomes[indice_do_maior]} com {maior_quantidade_clientes} clientes")

    elif opcao_escolhida == "3":
        print("\n" + "="*40)
        print("     BUSCAR RESTAURANTE    ")
        print("="*40)
        nome_para_busca = input("Digite o nome do restaurante para buscar: ").strip()
        
        for indice in range(len(lista_de_nomes)):
            if lista_de_nomes[indice].lower() == nome_para_busca.lower():
                print(f"\nDados de {lista_de_nomes[indice]}:")
                print(f"Localização: {lista_de_cidades[indice]} - {lista_de_estados[indice]}")
                print(f"Funcionários: {lista_de_funcionarios[indice]} | Clientes: {lista_de_clientes[indice]}")
                print(f"Faturamento: R$ {lista_de_faturamentos[indice]:.2f} | Nota: {lista_de_notas[indice]}")
                break
        else:
            print("Restaurante não encontrado.")

    elif opcao_escolhida == "4":
        print("\n" + "="*40)
        print("     ESTATÍSTICAS GERAIS    ")
        print("="*40)
        if len(lista_de_nomes) == 0:
            print("\nSem dados suficientes para gerar estatísticas.")
            continue
            
        total_restaurantes = len(lista_de_nomes)
        
        restaurante_maior_faturamento = lista_de_nomes
        maior_faturamento_encontrado = lista_de_faturamentos
        
        restaurante_menor_cancelamento = lista_de_nomes
        menor_cancelamento_encontrado = lista_de_pedidos_cancelados
        
        soma_faturamento_geral = 0
        soma_notas_geral = 0
        total_pedidos_cancelados_geral = 0
        total_pedidos_geral = 0
        
        soma_clientes_restaurantes_grandes = 0
        contador_restaurantes_grandes = 0
        
        for indice in range(total_restaurantes):
            soma_faturamento_geral += lista_de_faturamentos[indice]
            soma_notas_geral += lista_de_notas[indice]
            total_pedidos_cancelados_geral += lista_de_pedidos_cancelados[indice]
            total_pedidos_geral += (lista_de_pedidos_entregues[indice] + lista_de_pedidos_cancelados[indice])
            
            if lista_de_faturamentos[indice] > maior_faturamento_encontrado:
                maior_faturamento_encontrado = lista_de_faturamentos[indice]
                restaurante_maior_faturamento = lista_de_nomes[indice]
                
            if lista_de_pedidos_cancelados[indice] < menor_cancelamento_encontrado:
                menor_cancelamento_encontrado = lista_de_pedidos_cancelados[indice]
                restaurante_menor_cancelamento = lista_de_nomes[indice]
                
            if lista_de_funcionarios[indice] > 20:
                soma_clientes_restaurantes_grandes += lista_de_clientes[indice]
                contador_restaurantes_grandes += 1

        media_faturamento_geral = soma_faturamento_geral / total_restaurantes
        media_notas_geral = soma_notas_geral / total_restaurantes
        
        print(f"Restaurante com maior faturamento: {restaurante_maior_faturamento} (R$ {maior_faturamento_encontrado:.2f})")
        print(f"Restaurante com menor número de cancelamentos: {restaurante_menor_cancelamento} ({menor_cancelamento_encontrado} cancelamentos)")
        
        if contador_restaurantes_grandes > 0:
            print(f"Média de clientes em restaurantes com +20 funcionários: {soma_clientes_restaurantes_grandes / contador_restaurantes_grandes:.1f}")
        else:
            print("Média de clientes em restaurantes com +20 funcionários: N/A (Nenhum com +20 funcionários)")
            
        if total_pedidos_geral > 0:
            percentual_cancelados = (total_pedidos_cancelados_geral / total_pedidos_geral) * 100
            print(f"Percentual de pedidos cancelados: {percentual_cancelados:.2f}%")
        else:
            print("Percentual de pedidos cancelados: 0.00%")
            
        print(f"Média das notas dos clientes gerais: {media_notas_geral:.1f}")
        print(f"Média de faturamento geral: R$ {media_faturamento_geral:.2f}")
        
        quantidade_acima_media_faturamento = 0
        quantidade_nota_superior_a_8 = 0
        for indice in range(total_restaurantes):
            if lista_de_faturamentos[indice] > media_faturamento_geral:
                quantidade_acima_media_faturamento += 1
            if lista_de_notas[indice] > 8:
                quantidade_nota_superior_a_8 += 1
                
        print(f"Restaurantes com faturamento acima da média geral: {quantidade_acima_media_faturamento}")
        porcentagem_nota_8 = (quantidade_nota_superior_a_8 / total_restaurantes) * 100
        print(f"Porcentagem de restaurantes com nota superior a 8: {porcentagem_nota_8:.2f}%")
        print(f"Total geral de pedidos cancelados: {total_pedidos_cancelados_geral}")

    elif opcao_escolhida == "5":
        print("\n" + "="*40)
        print("     ATUALIZAR DADOS DE RESTAURANTE    ")
        print("="*40)
        nome_para_alterar = input("Digite o nome do restaurante que deseja atualizar: ").strip()
        
        for indice in range(len(lista_de_nomes)):
            if lista_de_nomes[indice].lower() == nome_para_alterar.lower():
                print(f"Modificando dados de {lista_de_nomes[indice]}. Pressione ENTER para manter o valor atual.")
                
                nova_cidade = input(f"Nova cidade [{lista_de_cidades[indice]}]: ").strip().title()
                if nova_cidade != "": 
                    lista_de_cidades[indice] = nova_cidade
                
                novo_estado = input(f"Novo estado [{lista_de_estados[indice]}]: ").strip().upper()
                if novo_estado != "": 
                    lista_de_estados[indice] = novo_estado
                
                while True:
                    entrada_func = input(f"Novos funcionários [{lista_de_funcionarios[indice]}]: ").strip()
                    if entrada_func == "": 
                        break
                    try:
                        valor_inteiro = int(entrada_func)
                        if valor_inteiro < 0:
                            print("\n*** Erro! Não pode ser negativo. ***")
                            continue
                        lista_de_funcionarios[indice] = valor_inteiro
                        break
                    except ValueError: 
                        print("\n*** Digite um número inteiro válido. ***")
                print("Dados atualizados com sucesso!")
                break
        else:
            print("Restaurante não encontrado.")

    elif opcao_escolhida == "6":
        print("\n" + "="*40)
        print("     REMOVER RESTAURANTE    ")
        print("="*40)
        nome_para_remover = input("Digite o nome do restaurante para deletar: ").strip()
        
        for indice in range(len(lista_de_nomes)):
            if lista_de_nomes[indice].lower() == nome_para_remover.lower():
                print(f"Removendo {lista_de_nomes[indice]} do sistema...")
                lista_de_nomes.pop(indice)
                lista_de_cidades.pop(indice)
                lista_de_estados.pop(indice)
                lista_de_funcionarios.pop(indice)
                lista_de_clientes.pop(indice)
                lista_de_faturamentos.pop(indice)
                lista_de_pedidos_entregues.pop(indice)
                lista_de_pedidos_cancelados.pop(indice)
                lista_de_notas.pop(indice)
                lista_de_pratos.pop(indice)
                print("Restaurante removido com sucesso!")
                break
        else:
            print("Restaurante não encontrado.")

    elif opcao_escolhida == "7":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("\n*** Opção inválida! Escolha um número de 1 a 7. ***")