##1. Simple Calculator
## Get two numbers and an operator (+, -, *, /).
## Use conditional statements to perform the selected operation.

a = int(input("Enter value for A: "))
b = int(input("Enter value for B: "))
operator = input("Enter operator (+,-,*,/): ")

if operator == "+":
    print("Addition: ", a+b)

elif operator == "-":
    print("Subraction: ", a-b)

elif operator == "*":
    print("Product: ", a*b)

elif operator == "/":
    print("Division: ", a/b)

else:
    print("Wrong Operator")
