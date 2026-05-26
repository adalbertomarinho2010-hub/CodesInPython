Distance = float (input ("Type the distance (Km): "))
AmountGas = float (input ("Type the consume of gas (Km/L): "))
PriceGas = float (input ("Type the price of gas: "))

GasNecessary = Distance / AmountGas
AmountValue = PriceGas * GasNecessary

print ("Total cust in the trail: %.2f"%(AmountValue))
print ("The Amount of gas necessary: %.2f"% (GasNecessary))