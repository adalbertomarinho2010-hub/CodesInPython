nome_restaurante = []
cidade = []
estado = []
quant_funcionarios = []
quant_clientes_mes = []
faturamento_mensal = []
quant_pedidos_entregues = []
quant_pedidos_cancelados = []
nota_media = []
quant_pratos = []

x = 1

while x != 0:
    print("\n========================================================================")
    print("          SEJA MUITO BEM VINDO(A) AO NOSSO SISTEMA DE RESTAURANTE        ")
    print("=========================================================================")

    print("\n1. Cadastro Restaurante\n2. Exibir relatório completo\n3. Buscar Restaurante pelo Nome\n4. Mostrar Estatísticas Gerais\n5. Atualizar Dados de Restaurante\n6. Remover Restaurante\n7. Encerar sistema\n")
    escolha = str (input("\nDigite a sua escolha: "))

    if escolha == "1":

        print("\n==========================================================")
        print("          MENU DE CADASTRO DE RESTAURANTE                  ")
        print("===========================================================")
        
        dig_nome_restaurante = str (input("\nDigite o nome do restaurante: "))
        if dig_nome_restaurante != "":
            nome_restaurante.append (dig_nome_restaurante)
        
        dig_cidade = str (input("Digite a cidade do restaurante: "))
        if dig_cidade != "":
            cidade.append (dig_cidade)

        dig_estado = str (input("Digite o estado do restaurante: "))
        if dig_estado != "":
            estado.append (dig_estado)

        dig_quant_funcionarios = int (input("Digite a quantidade de funcionários do restaurante: "))
        if dig_quant_funcionarios != "":
            quant_funcionarios.append (dig_quant_funcionarios) 

        dig_quant_clientes_mes = int (input("Digite a quantidade de clientes do restaurante mensalmente: "))
        if dig_quant_clientes_mes != "":
            quant_clientes_mes.append (dig_quant_clientes_mes)

        dig_faturamento_mensal = float (input("Digite o faturamento mensal do restaurante: "))
        if dig_faturamento_mensal != "":
            faturamento_mensal.append (dig_faturamento_mensal)    

        dig_quant_pedidos_entregues = int (input("Digite a quantidade de pedidos entregues do restaurante: "))
        if dig_quant_pedidos_entregues != "":
            quant_pedidos_entregues.append (dig_quant_pedidos_entregues)        

        dig_quant_pedidos_cancelados = int (input("Digite a quantidade de pedidos cancelados do restaurante: "))
        if dig_quant_pedidos_cancelados != "":
            quant_pedidos_cancelados.append (dig_quant_pedidos_cancelados)        

