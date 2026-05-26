x = 1
while x != 0:
  print ("========== Menu da Calculadora =========")
  print ("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair")
  opcao = int (input("Escolha a opção desejada: \n"))

  if opcao == 1:
    print ("========== Menu de Adição =========")
    n1 = float (input("Digite o primeiro numero: "))
    n2 = float (input("Digite o segundo numero: "))
    result = n1 + n2
    print (n1," + ",n2," = %.2f"% (result))
    print ("\n")
    continue
  
  if opcao == 2:
    print ("========== Menu de Subtração =========")
    n1 = float (input("Digite o primeiro numero: "))
    n2 = float (input("Digite o segundo numero: "))
    result = n1 - n2
    print (n1," - ",n2," = %.2f"% (result))
    print ("\n")
    continue
  
  if opcao == 3:
    print ("========== Menu de Multiplicação =========")
    n1 = float (input("Digite o primeiro numero: "))
    n2 = float (input("Digite o segundo numero: "))
    result = n1 * n2
    print (n1," x ",n2," = %.2f"% (result))
    print ("\n")
    continue
  
  if opcao == 4:
    print ("========== Menu de Divisão =========")
    n1 = float (input("Digite o primeiro numero: "))
    n2 = float (input("Digite o segundo numero: "))
    result = n1 / n2
    print (n1," / ",n2," = %.2f"% (result))
    print ("\n")
    continue
  
  if opcao == 0:
    print ("Saindo da calculadora...")
    break