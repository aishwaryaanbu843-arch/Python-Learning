num = int(input("Enter the number: "))
rev = 0
original = num
while num != 0:
    last = num % 10
    rev = (rev * 10)+ last
    num = num // 10

if original == rev:
    print("It is a palindrome number")
else:
    print("It is not a palindrome")

