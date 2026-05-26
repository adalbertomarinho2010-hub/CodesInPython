while True:
    Value = int (input("Digite 1 ou 0 para sair: "))
    if Value == 1:
        print ("\nCorrect value \n")
    else:
        print ("\nValue to quit\n")
        break

while True:
    Value = int (input("Digite 1 ou 0 para encerrar: "))
    if Value <= 1: 
        continue
        print ("Maior que um")   
    if Value > 1:
        print ("Maior que um") 
        break