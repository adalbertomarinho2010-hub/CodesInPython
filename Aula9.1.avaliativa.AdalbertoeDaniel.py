cpf = []
nome = []
senha = []
endereco = []
telefone = []
agencia = []
numero_da_conta = []
saldo = []
email = []
data_de_nascimento = []
tipo_de_conta = []
limite_de_credito = [] 
x = 1

while x != 0:
    print("=========================================================")
    print("                    MENU DE ENTRADA                      ")
    print("=========================================================")
    print("\n1. Entrar no banco\n2. Sair do banco")
    escolha = str(input("\nEscolha a opção desejada: "))

    if escolha == "1":
        senha_login = str(input("\nDigite sua senha para entrar no banco: "))
        Verificando = False
        opcao = 1

        while opcao != "0":
            
            if senha_login == "123": ###Senha utilizada apenas para entrar como senha primária
                print("\n=========================================================")
                print("          SEJA MUITO BEM VINDO(A) AO NOSSO BANCO         ")
                print("=========================================================")

                print("\n1. Cadastro de cliente\n2. Consulta de Cadastro\n3. Exclusão de Cadastro\n4. Ver Saldo\n5. Depósito\n6. Saque\n7. Editar\n0. Sair\n")
                escolha = str(input("Digite a opção desejada: "))
                if escolha == "1":
                    print("=========================================================")
                    print("                 CADASTRANDO CLIENTE                     ")
                    print("=========================================================")
                    new_cliente = str(input("\nDigite o nome completo: "))
                    if new_cliente != "":
                        nome.append(new_cliente)

                    new_cpf = str(input("Digite o cpf: "))
                    if new_cpf != "":
                        cpf.append(new_cpf)
                    
                    new_senha = str(input("Digite a senha: "))
                    if new_senha != "":
                        senha.append(new_senha)
                    
                    new_endereco = str(input("Digite o endereço: "))
                    if new_endereco != "":
                        endereco.append(new_endereco)

                    new_telefone = str(input("Digite o telefone: "))
                    if new_telefone != "":
                        telefone.append(new_telefone)

                    while True:
                        try:
                            new_agencia = int(input("Digite a agência: ")) ###Apenas números
                            if new_agencia != "":
                                agencia.append(new_agencia)
                                break
                        except ValueError:
                            print ("\n(***Por favor, digite apenas números!***)\n")

                    while True:
                        try:
                            new_numero_da_conta = int(input("Digite o numero da conta: ")) ###Apenas números
                            if new_numero_da_conta != "":
                                numero_da_conta.append(new_numero_da_conta)
                                break
                        except ValueError:
                            print ("\n(***Por favor, digite apenas números!***)\n")
                    
                    while True:
                        try:
                            new_saldo = float(input("Digite o saldo da conta (R$): "))
                            if new_saldo != "":
                                saldo.append(new_saldo)
                                break
                        except ValueError:
                            print("\n(***Não é um valor monetário****)\n")
                    
                    
                    new_email = str(input("Digite o email: "))
                    if new_email!= "":
                        email.append(new_email)

                    new_data_de_nascimento = str(input("Digite a data de nascimento: ")) ###Apenas número
                    if new_data_de_nascimento!= "":
                        data_de_nascimento.append(new_data_de_nascimento)
                    
                    new_tipo_de_conta = str(input("Digite o tipo da conta: "))
                    if new_tipo_de_conta!= "":
                        tipo_de_conta.append(new_tipo_de_conta)

                    while True:
                        try:
                            new_limite_de_credito = float(input("Digite o limite de crédito (R$): ")) ###Apenas número
                            if new_limite_de_credito!= "":
                                limite_de_credito.append(new_limite_de_credito)
                                break
                        except ValueError:
                            print("\n(***Não é um valor monetário****)\n")
                
                if escolha == "2":
                    print("=========================================================")
                    print("                 CONSULTA DE CADASTRO                    ")
                    print("=========================================================")
                    cpf_digitado = str(input("\nDigite o seu CPF: "))
                    if cpf_digitado in cpf:
                        indice = cpf.index (cpf_digitado)
                        print (f"Nome: {nome[indice]}")
                        print (f"CPF: {cpf[indice]}")
                        print (f"Senha: {senha[indice]}")
                        print (f"Endereço: {endereco[indice]}")
                        print (f"Telefone: {telefone[indice]}")
                        print (f"Agência: {agencia[indice]}")
                        print (f"Número da Conta: {numero_da_conta[indice]}")
                        print (f"Saldo: R$ {saldo[indice]}")
                        print (f"Email: {email[indice]}")
                        print (f"Data de Nascimento: {data_de_nascimento[indice]}")
                        print (f"Tipo de Conta: {tipo_de_conta[indice]}")
                        print (f"Limite de Crédito: {limite_de_credito[indice]}")
                    else:
                        print ("\nCPF não encontrado...")

                if escolha == "3":
                    print("=========================================================")
                    print("                 EXCLUSÃO DE CADASTRO                    ")
                    print("=========================================================")
                    cpf_excluir = str(input("\nDigite o seu CPF: "))
                    if cpf_excluir in cpf:
                        indice = cpf.index (cpf_excluir)
                        nome.pop (indice)
                        cpf.pop (indice)
                        senha.pop (indice)
                        endereco.pop (indice)
                        telefone.pop (indice)
                        agencia.pop (indice)
                        numero_da_conta.pop (indice)
                        saldo.pop (indice)
                        email.pop (indice)
                        data_de_nascimento.pop (indice)
                        tipo_de_conta.pop (indice)
                        limite_de_credito.pop (indice)

                        print("\nSeu cadastro foi excluido com sucesso!")
                    else:
                        print ("\nCPF não encontrado...") 

                if escolha == "4":
                    print("=========================================================")
                    print("                     VERIFICAR SALDO                     ")
                    print("=========================================================")
                    
                    while True:
                        try:
                            numero_da_conta_digitado = int(input("\nDigite o numero da sua conta: "))
                            if numero_da_conta_digitado in numero_da_conta:
                             senha_digitada = str(input("Digite sua senha: "))
                             if senha_digitada in senha:
                                indice = numero_da_conta.index (numero_da_conta_digitado) 
                                print (f"\n*** Seu saldo atual é: R$ {saldo[indice]} ***")
                                break
                             else:
                                print ("Senha incorreta digitada.")
                            else:
                             print ("\nNumero da conta não encontrado...")
                        except ValueError:
                           print ("\nPor favor, digite números!") 

                if escolha == "5":
                    print("=========================================================")
                    print("                     DEPÓSITO DE SALDO                   ")
                    print("=========================================================")

                    while True:
                        try:
                            numero_da_conta_digitado = int(input("\nDigite o numero da sua conta: "))
                            if numero_da_conta_digitado in numero_da_conta:
                                valor = float (input("\nDigite o valor que deseja depositar (R$): ")) 
                                saldo [indice] += valor
                                print ("\n*** O valor depositado foi (R$): ",valor," ***")
                                break
                            else:
                                print ("\nNumero da conta não encontrado...")
                                break
                        except ValueError:
                            print ("\nPor favor, digite números!")


                if escolha == "6":
                    print("=========================================================")
                    print("                     SACAR SALDO                         ")
                    print("=========================================================")

                    while True:
                        try:
                            numero_da_conta_digitado = int(input("\nDigite o numero da sua conta: "))
                            if numero_da_conta_digitado in numero_da_conta:
                                senha_digitada = str(input("Digite sua senha: "))
                                if senha_digitada in senha:
                                 indice = numero_da_conta.index (numero_da_conta_digitado)
                                 valor = float (input("\nDigite o valor que deseja sacar (R$): "))  
                                 if valor < saldo[indice]:
                                    saldo [indice] -= valor
                                    print ("Saque realizado com sucesso no valor de (R$): ",valor)
                                    break
                                 if valor > saldo[indice]:
                                    print ("Saldo insuficiente para sacar!")
                                    break
                                else:
                                 print ("Senha incorreta digitada.")
                                 break
                            else:
                                print ("\nNumero da conta não encontrado...")
                        except ValueError:
                            print ("\nPor favor, digite números!")

                
                if escolha == "7":
                    print("=========================================================")
                    print("                     MENU DE EDIÇÃO                      ")
                    print("=========================================================")
                    print ("Selecione qual dado você deseja alterar:\n1. Nome\n2. Endereço\n3. Telefone\n4. CPF\n5. Agência\n6. Número da conta\n7. Email\n8. Data de nascimento\n9. Tipo de conta\n10. Senha\n11. Limite de crédito")
                    escolha_edicao = str(input("\nSelecione qual informação você deseja alterar: "))

                    if escolha_edicao == "1":

                        cpf_digitado = str(input("\nDigite o seu CPF: "))
                        if cpf_digitado in cpf:
                            indice = cpf.index (cpf_digitado)
                            novo_nome = str(input("\nDigite o nome para qual você deseja mudar: "))
                            nome[indice] = novo_nome
                            print("Informação alterada para: ",nome[indice])  
                        
                    if escolha_edicao == "2":

                        cpf_digitado = str(input("\nDigite o seu CPF: "))
                        if cpf_digitado in cpf:
                            indice = cpf.index (cpf_digitado)
                            novo_endereco = str(input("\nDigite o endereço para qual você deseja mudar: "))
                            endereco[indice] = novo_endereco
                            print("Informação alterada para: ",endereco[indice])    
                    
                    if escolha_edicao == "3":

                        cpf_digitado = str(input("\nDigite o seu CPF: "))
                        if cpf_digitado in cpf:
                            indice = cpf.index (cpf_digitado)
                            novo_telefone = str(input("\nDigite o telefone para qual você deseja mudar: "))
                            telefone[indice] = novo_telefone
                            print("Informação alterada para: ",telefone[indice])

                    if escolha_edicao == "4":

                        cpf_digitado = str(input("\nDigite o seu CPF: "))
                        if cpf_digitado in cpf:
                            indice = cpf.index (cpf_digitado)
                            novo_cpf = str(input("\nDigite o CPF para qual você deseja mudar: "))
                            cpf[indice] = novo_cpf
                            print("Informação alterada para: ",cpf[indice])

                    if escolha_edicao == "5":
                        
                        while True:
                            try:
                                cpf_digitado = str(input("\nDigite o seu CPF: "))
                                if cpf_digitado in cpf:
                                    indice = cpf.index (cpf_digitado)
                                    nova_agencia = int(input("\nDigite a agência para qual você deseja mudar: "))
                                    agencia[indice] = nova_agencia
                                    print("Informação alterada para: ",agencia[indice])
                                    break
                            except ValueError:
                                print ("\nDigite apenas números, por favor!")

                    if escolha_edicao == "6":
                        
                        while True:
                            try:
                                cpf_digitado = str(input("\nDigite o seu CPF: "))
                                if cpf_digitado in cpf:
                                    indice = cpf.index (cpf_digitado)
                                    novo_numero = int(input("\nDigite o número da conta para qual você deseja mudar: "))
                                    numero_da_conta[indice] = novo_numero
                                    print("Informação alterada para: ",numero_da_conta[indice])
                                    break
                            except ValueError:
                                print ("\nDigite apenas números, por favor!") 

                    if escolha_edicao == "7":

                        cpf_digitado = str(input("\nDigite o seu CPF: "))
                        if cpf_digitado in cpf:
                            indice = cpf.index (cpf_digitado)
                            novo_email = str(input("\nDigite o email para qual você deseja mudar: "))
                            email[indice] = novo_email
                            print("Informação alterada para: ",email[indice])

                    if escolha_edicao == "8":

                        cpf_digitado = str(input("\nDigite o seu CPF: "))
                        if cpf_digitado in cpf:
                            indice = cpf.index (cpf_digitado)
                            nova_data = str(input("\nDigite a data de nascimento para qual você deseja mudar: "))
                            data_de_nascimento[indice] = nova_data
                            print("Informação alterada para: ",data_de_nascimento[indice])

                    if escolha_edicao == "9":

                        cpf_digitado = str(input("\nDigite o seu CPF: "))
                        if cpf_digitado in cpf:
                            indice = cpf.index (cpf_digitado)
                            nova_conta = str(input("\nDigite o tipo de conta para qual você deseja mudar: "))
                            tipo_de_conta[indice] = nova_conta
                            print("Informação alterada para: ",tipo_de_conta[indice]) 

                    if escolha_edicao == "10":

                        cpf_digitado = str(input("\nDigite o seu CPF: "))
                        if cpf_digitado in cpf:
                            indice = cpf.index (cpf_digitado)
                            nova_senha = str(input("\nDigite a senha para qual você deseja mudar: "))
                            senha[indice] = nova_senha
                            print("Informação alterada para: ",senha[indice])

                    if escolha_edicao == "11":

                        while True:
                            try:
                                cpf_digitado = str(input("\nDigite o seu CPF: "))
                                if cpf_digitado in cpf:
                                    indice = cpf.index (cpf_digitado)
                                    novo_limite = int(input("\nDigite o novo limite para qual você deseja mudar: "))
                                    limite_de_credito[indice] = novo_limite
                                    print("Informação alterada para: ",limite_de_credito[indice])
                                    break
                            except ValueError:
                                print ("\nDigite apenas números, por favor!") 

                if escolha == "0":
                    print("\nSaindo...")
                    opcao = 0

            else:
                print ("\nSenha incorreta...\n")
                break
           
    if escolha == "2":
        print("=========================================================")
        print("\nFechando o banco...\n")
        x = 0