Side1 = float (input ("Type the cm² of the first side: "))
Side2 = float (input ("Type the cm² of the second side: "))
Side3 = float (input ("Type the cm² of the third side: "))
if (Side1 == Side2 == Side3):
    print ("Your triangle type is: Equilátero")
elif (Side1 == Side2 or Side1 == Side3 or Side2 == Side1 or Side2 == Side3 or Side3 == Side1 or Side3 == Side2):
    print ("Your triangle type is: Isósceles")
elif (Side1 != Side2 and Side1 != Side3 and Side3 != Side1):
    print ("Your triangle type is: Escaleno")
