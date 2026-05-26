numerator = 0
while numerator <= 1000:
    print (numerator)
    numerator += 5

print ("End") 
print ("Value of numerator after while is: ",numerator)
print ("\n")

addition = 0
num = int (input("Type a number: "))
while num != 0:
    addition += num
    print ("The value now is: ",addition)
    num = int (input("Type a number: "))

print ("Total : ",addition)
print ("\n")

qnt = 0
addition = 0
num = int (input("Type a number: "))
while num != 0:
    addition += num
    qnt += 1
    print ("The value now is: %.2f"%(addition))
    print ("The qnt now is: ",qnt)
    print ("\n")
    num = int (input("Type a number: "))

average = addition / qnt
print ("Your average has addition these number times in total: ",qnt)
print ("The average is: %.2f"%(average))
print ("\n")

fruits = ["Banana","Maça","Uva","Pera","Abacaxi","Kiwi"]
print (len(fruits))

i = 0
while i < len(fruits):
    print (fruits[i])
    i = i + 1

print ("\n")

i = 50
while i >= 0:
    print (i)
    i -= 1

print ("End")
print ("\n")

x = 10
while not (x == 0):
    x = x - 1
    if x % 2 != 0:
        print (x)

print ("\n")

ended = False
par = imp = 0
while (not ended):
    num = int (input("Type a number, or zero to end: "))
    if num == 0:
        ended = True
    else:
        if num % 2 == 0:
            par = par + 1
        else:
            imp = imp + 1

print ("pares = ",par )
print ("impares = ",imp )