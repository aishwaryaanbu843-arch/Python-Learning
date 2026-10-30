##Salary Bonus
## Get salary and years of experience. 
##
## Experience ≥ 5 years → 10% bonus 
##
## Experience 2–4 years → 5% bonus 
##
## Less than 2 years → No bonus

salary = int(input("Enter your salary: "))
experience = int(input("Enter your years of experience: "))

if experience>=5:
    bonus = salary*10/100
    finalSalary = salary + bonus

elif experience>=4:
    bonus = salary*5/100
    finalSalary = salary + bonus

else:
    print("No bonus because you have less than 2 years of experience")

print("The total salary is: ", finalSalary)
