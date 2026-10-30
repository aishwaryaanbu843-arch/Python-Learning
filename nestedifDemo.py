##SHOPPING DISCOUNT:

amount = int(input("Enter purchase amount: "))
member = input("Are you a member? (yes/no): ")

if amount > 5000:
    if member == "yes":
        discount = amount * 0.20
    else:
        discount = amount * 0.10

else:
    if member == "yes":
        discount = amount * 0.10
    else:
        discount = amount * 0.05

final_amount = amount - discount

print("Discount: ₹" + str(discount))
print("Final amount: ₹" + str(final_amount))

