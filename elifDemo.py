ElECTRICITY BILL:
    
bill = int(input("Enter bill amount:"))
if(bill>0 and bill<=100):
    print("2 per unit")
elif(bill>101 and bill<=200):
    print("3 per unit")
elif(bill>201 and bill<=300):
    print("5 per unit")
else:
    print("7 per unit")

TEMPERATURE CHECKER:

temp = int(input("Enter temperature in celsius:"))
if(temp<15):
    print("Cold")
elif(temp>15 and temp<=25):
    print("Cool")
elif(temp>26 and temp<=35):
    print("Warm")
else:
    print("Hot")

ATM WITHDRAWL:

balance = int(input("Enter account balance:"))
withdrawl = int(input("Enter withdrawl amount:"))
if(withdrawl <= 0):
    print("Invalid amount")
elif(withdrawl > balance):
    print("Insufficient balance")
else:
    print("Remaining balance:", balance - withdrawl)





