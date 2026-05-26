Salary = float (input ("Type your salary: "))
if (Salary < 500.00):
    NewSalary = Salary * 1.15
    print ("Your salary now is: %.2f"% (NewSalary))
elif (Salary > 500.00 or Salary <= 1000.00):
    NewSalary = Salary * 1.10
    print ("Your salary now is: %.2f"% (NewSalary))
elif (Salary < 1000.00):
    NewSalary = Salary * 1.05
    print ("Your salary now is: %.2f"% (NewSalary))