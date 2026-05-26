#for i in range (1,11):
 #   for j in range (1,11):
  #      k = i * j
   #     print (i," x ",j," = ",k)

#for n in range (1,51,2):
    #print (n)

n1 = int (input("Digite o primeiro número: "))
n2 = int (input("\nDigite o segundo número: "))
n3 = int (input("\nDigite o terceiro número: "))
n4 = int (input("\nDigite o quarto número: "))
n5 = int (input("\nDigite o quinto número: "))
soma = 0
for n1 in range (0,n1):
    soma = 0
    soma = soma + n1 + n2 + n3 + n4 + n5
    media = soma / 5
    print (n1)
    
print ("\nA soma dos números é: ",soma)
print ("\nA média desses números é: %.2f"%(media))