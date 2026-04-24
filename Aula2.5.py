Product1 = float (input ("Type the value of the first product: ")) 
Product2 = float (input ("Type the value of the second product: "))
Product3 = float (input ("Type the value of the three product: ")) 
Product4 = float (input ("Type the value of the four product: "))
Product5 = float (input ("Type the value of the five product: "))
Money = float (input ("Type the amount of payment that you want: "))
PaymentForm = str (input("Type the payment form: " ))

InicialValue1 = Product1 + Product2 + Product3 + Product4 + Product5
InicialValue2 = Product1 + Product2 + Product3 + Product4 + Product5
InicialValue3 = Product1 + Product2 + Product3 + Product4 + Product5

Discount1 = InicialValue1 * 0.10
Discount2 = InicialValue2 * 0.05

FinalValue1 = Product1 + Product2 + Product3 + Product4 + Product5 - Discount1
FinalValue2 = Product1 + Product2 + Product3 + Product4 + Product5 - Discount2
FinalValue3 = Product1 + Product2 + Product3 + Product4 + Product5

print ("In vist: 10","%", "discount = ",Discount1,",","Final Value: ",FinalValue1)
print ("In card: 5","%","discount = ",Discount2,",","Final Value: ",FinalValue2)
print ("Parcel: 0","%","discount = 0",",","Final Value: ",FinalValue3)
