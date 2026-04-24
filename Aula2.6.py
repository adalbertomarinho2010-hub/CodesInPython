Name = str (input ("Type your Name: "))
Product1 = float (input ("Type the value of the first product: ")) 
Product2 = float (input ("Type the value of the second product: "))
Product3 = float (input ("Type the value of the three product: ")) 
InicialValue = Product1 + Product2 + Product3
AverageValue = (Product1 + Product2 + Product3) / 3
Discount1 = InicialValue * 0.12
TotalValue1 = InicialValue - Discount1
Discount2 = TotalValue1 * 0.05
TotalValue2 = TotalValue1 - Discount2
LastValue = TotalValue2
print ("The name of the costumer:",Name)
print ("The total value with no discount: %.2f" % (InicialValue))
print ("The average value with no discount is: %.2f" % (AverageValue))
print ("The value: 12","%","discount = %.2f"% (Discount1),".","Second Value: %.2f"%(TotalValue1))
print ("The value with 12","%","and","5","%","discount = %.2f"%(Discount1 + Discount2),".","Final Value: %.2f"%(LastValue))