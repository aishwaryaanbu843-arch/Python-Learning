##Movie Ticket Price 
##
##Get age and show timing.
##
##Rules:
##
## Age below 12 → Child ticket 
##
## Age 12–59 → Adult ticket 
##
## Age 60 or above → Senior citizen ticket 
##
## If show timing is "morning", give an additional discount.

age = int(input("Enter your age: "))
show = input("Enter type of show (Morning, Afternoon, Evening, Night): ").lower()
ticket = 200

if age<12:
    print("Child ticket")

elif age<60:
    print("Adult ticket")

else:
    print("Senior citizen ticket")


if show == "morning":
    discount = ticket * 15 / 100
    finalAmount = ticket - discount
    print("Morning discount: 15%")

else:
    finalAmount = ticket
    print("There is no discount")

print("The total ticket price is: ", finalAmount)

