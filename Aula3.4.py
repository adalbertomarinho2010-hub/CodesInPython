Note1 = float (input ("Type the first note: "))
Note2 = float (input ("Type the second note: "))
Note3 = float (input ("Type the three note: "))
Note4 = float (input ("Type the four note: "))

AverageNote = (Note1 + Note2 + Note3 + Note4) / 4

if AverageNote >= 4:
    print ("Your average note is: ",AverageNote," = Aproved")
elif AverageNote >=5.0:
    print ("Your average note is: ",AverageNote," = Exam")
else:
    print ("Your average note is: ",AverageNote," = Reproved")



