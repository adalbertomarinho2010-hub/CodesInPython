fruits = ["Banana","Maça","Uva","Pera","Abacaxi","Kiwi"]

for fruit in fruits:
    print (fruit)
    print ("\n")

list = [99,88,56,43,54,22,34,76,89,23]
list.sort ()
for number in list:
    print (number)
    print ("\n")

for x in range (0,101,5):
    print (x)

print ("\n")

num = int (input("Type a number: "))
l = 1,2,3,4,5,6,7,8,9,10
for i in l:
    result = i * num
    print (num," x ",i," = ",result)
print ("\n")


num = int (input("Type a number: "))
cont = 1
while cont <= 10:
    result = cont * num
    cont = cont + 1
    print (num," x ",i," = ",result)
print ("\n")