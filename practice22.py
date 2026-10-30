num = int(input("Enter the number: "))
i = 2
while (i < num):
    if(num % i == 0):
        print("Not prime")
    else:
        print("It is a prime number")
    i += 1
