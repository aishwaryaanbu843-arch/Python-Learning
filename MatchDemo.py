print("Choose: \n  +  Addition\n  -  Subraction\n *  Multiplication\n /  Division\n")
      
operator = input("Enter operator: ")
match operator:
    case "+":
        a = int(input("Enter value for A: "))
        b = int(input("Enter value for B: "))
        print("Addition of a and b: ", a+b)
    case "-":
        a = int(input("Enter value for A: "))
        b = int(input("Enter value for B: "))
        print("Subraction of a and b: ", a-b)
    case "*":
        a = int(input("Enter value for A: "))
        b = int(input("Enter value for B: "))
        print("Multiplication of a and b: ", a*b)
    case "/":
        a = int(input("Enter value for A: "))
        b = int(input("Enter value for B: "))
        print("Division of a and b: ", a/b)
    case _:
        print("Invalid")
        
        
    
        
