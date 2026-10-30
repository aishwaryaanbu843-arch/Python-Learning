##LIST OF NUMBERS:
##numbers = []
##for i in range(5):
##    num = int(input("Enter the number: "))
##    numbers.append(num)
##print("List: ", numbers)
##
####SUM:
##numbers = []
##sum = 0
##for i in range(5):
##    num = int(input("Enter the number: "))
##    numbers.append(num)
##    sum = sum + num
##print("Sum: ", sum)
##
####COUNT EVEN NUMBERS:
##
##numbers = []
##count = 0
##for i in range(10):
##    num = int(input("Enter the number: "))
##    numbers.append(num)
##for num in numbers:
##    if num % 2 == 0:
##        count = count+1
##print("Even numbers: ", count)
##
####SEARCH NUMBERS:
##
##numbers = []
##for i in range(5):
##    num = int(input("Enter the numbers: "))
##    numbers.append(num)
##search = int(input("Enter the number to search: "))
##
##if search in numbers:
##    print("Number is present")
##else:
##    print("Number is not present")
##
####REVERSE A LIST:
##
##numbers = []
##for i in range(5):
##    num = int(input("Enter the number: "))
##    numbers.append(num)
##for i in range(4, -1, -1):
##    print(numbers[i])

##LARGEST NUMBERS:
##    4. Find Largest Number
##   Get 5 numbers and find the largest number.
##   Do not use max().

##numbers = []
##for i in range(5):
##    num = int(input("Enter the number: "))
##    numbers.append(num)
##    largest = 0
##for num in numbers:
##    if num > largest:
##        largest = num
##print("The largest number: ",largest)

##5. Find Smallest Number
##   Get 5 numbers and find the smallest number.
##   Do not use min().
##

##numbers = []
##for i in range(5):
##    num = int(input("Enter the number: "))
##    numbers.append(num)
##    smallest = num
##for num in numbers:
##    if num < smallest:
##        smallest = num
##print("The smallest numbers: ", smallest)

##7. Count Occurrences
##   Get a list and a number from the user.
##   Find how many times the number occurs.
##   Do not use count().

numbers = []
count = 0
number = int(input("Enter the number for your list: "))
for i in range(5):
    num = int(input("Enter the numbers: "))
    number = int(input("Enter the number for your list: "))
    numbers.append(num)
for num in numbers:
    if num == numbers:
        count = count + 1
print("Repeated numbers: ", count)
    



