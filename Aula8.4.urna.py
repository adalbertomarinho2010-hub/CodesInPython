x = 1
voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto_nulo = 0
voto_branco = 0
while x != 0:
  print ("========== Menu da Urna =========")
  print ("1 - Kaneki\n2 - Rise\n3 - Arima\n4 - Touka\nNada - Voto Nulo\n5 - Voto em Branco\n0 - Sair\n")
  opcao = int (input("Escolha a opção desejada: "))

  if opcao == 1:
    voto1 = voto1 + 1
    print ("\nA quantidade de votos do candidato Kaneki é: ",voto1,"\n")
    continue
  
  if opcao == 2:
    voto2 = voto2 + 1
    print ("\nA quantidade de votos da candidata Rise é: ",voto2,"\n")
    continue
  
  if opcao == 3:
    voto3 = voto3 + 1
    print ("\nA quantidade de votos do candidato Arima é: ",voto3,"\n")
    continue
  
  if opcao == 4:
    voto4 = voto4 + 1
    print ("\nA quantidade de votos da candidata Touka é: ",voto4,"\n")
    continue
  
  if opcao == "":
    voto_nulo = voto_nulo + 1
    print ("\nA quantidade de votos nulos é: ",voto_nulo,"\n")
    continue
  
  if opcao == 5:
    voto_branco = voto_branco + 1
    print ("\nA quantidade de votos em branco é: ",voto_branco,"\n")
    continue
  
  if opcao == 0:
    print ("Saindo da Urna...")
    break
  
  if voto1 > voto2 and  voto1 > voto3 and  voto1 > voto4 and  voto1 > voto_branco and  voto1 > voto_nulo:
    ganhador = "\nO ganhador foi o canditato Kaneki - 1."

  if voto2 > voto1 and  voto2 > voto3 and  voto2 > voto4 and  voto2 > voto_branco and  voto2 > voto_nulo:
    ganhador = "\nA ganhadora foi a canditata Rise - 2."

  if voto3 > voto1 and  voto3 > voto2 and  voto3 > voto4 and  voto3 > voto_branco and  voto3 > voto_nulo:
    ganhador = "\nO ganhador foi o canditato Arima - 3."

  if voto4 > voto1 and  voto4 > voto2 and  voto4 > voto3 and  voto4 > voto_branco and  voto4 > voto_nulo:
    ganhador = "\nA ganhadora foi a canditata Touka - 4."

  total_votos = (voto1 + voto2 + voto3 + voto4 + voto_branco + voto_nulo)
  print ("\nA quantidade total de votos foi de: ",total_votos)