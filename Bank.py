##4. Bank Loan Eligibility 
##
##Get:
##
## Age 
##
## Salary 
##
## Credit score 
##
## Employment status 
##
##Loan is approved only if:
##
## Age is between 21 and 60 
##
## Salary ≥ ₹25,000 
##
## Credit score ≥ 700 
##
## Employment status is "employed"
##
##give appropriate else messages.

age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))
Credit_Score = int(input("Enter your Credit Score: "))
status = input("Enter status (Employed, Unemployed): ").lower()

if age>21 and age<=60 and salary >= 25000 and Credit_Score >= 700 and status == "employed": 
    print("Loan is approved")
else:
    print("Loan not approved")

