Note1 = float (input ("Type your first note: "))
Note2 = float (input ("Type your second note: "))
AverageNote = (Note1 + Note2) / 2
if (AverageNote >= 7 and AverageNote < 10):
    print ("Aproved! Your note is: %.2f"% (AverageNote))
elif (AverageNote < 7 ):
    print ("Reproved! Your note is: %.2f"% (AverageNote))
elif (AverageNote == 10):
    print ("Aproved with perfect note! Your note is: %.2f"% (AverageNote))