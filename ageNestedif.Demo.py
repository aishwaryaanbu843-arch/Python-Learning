##age = int(input("Enter your age: "))
##id = True
##
##if age>=18:
##    if id:
##        print("Entry Allowed")
##    else:
##        print("No entry")
##
##else:
##    print("Invalid")


##num = 10
##if num > 5:
##    if num < 15:
##        print("A")


##marks = int(input("Enter marks: "))
##hallTicket = False
##
##if marks>=25:
##    if marks>=80:
##        if hallTicket:
##            print("Distinction rank")
##    else:
##        print("Pass")
##else:
##    print("You dont have an hallticket")

amount = int(input("Enter purchase amount: "))
member = input("Are you a member? (yes/no): ")

if amount > 1000:
    if member == "yes":
        discount = amount * 0.20
    else:
        discount = amount * 0.10

else:
    print("No discount")

final_amount = amount - discount

print("Discount: " + str(discount))
print("Final amount: " + str(final_amount))


