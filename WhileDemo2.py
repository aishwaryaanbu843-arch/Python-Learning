num = int(input("Enter the number: "))
last = 0
rev = 0
while (num != 0):
    last = num % 10
    rev = (rev*10)+last
    num = num // 10
print("The reverse number is: ",rev)
    


##1. find the largest digit (to find: larges number is 9)
##2. print the even digits
##3. find weather the number is palindrome or not. (check 121 = 121)


