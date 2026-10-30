##7. Count Occurrences
##   Get a list and a number from the user.
##   Find how many times the number occurs.
##   Do not use count()

##numbers = []
##count = 0
##for i in range(5):
##    num = int(input("Enter the numbers: "))
##    numbers.append(num)
##search = int(input("Enter the number to be searched: "))
##for num in numbers:
##    if num == search:
##        count = count + 1
##print("Occurences: ", count)

##9. Separate Even and Odd
##   Get a list of numbers and create two separate lists:
##   Even numbers
##   Odd numbers
##
##10. Separate Positive and Negative
##    Get a list of numbers and create two separate lists:
##    Positive numbers
##    Negative numbers

##numbers = []
##even = []
##odd = []
##for i in range(5):
##    num = int(input("Enter the numbers: "))
##    numbers.append(num)
##for num in numbers:
##    if num % 2 == 0:
##        even.append(num)
##    else:
##        odd.append(num)
##print("Even numbers: ", even)
##print("Odd numbers: ", odd)


##numbers = []
##positive = []
##negative = []
##for i in range(5):
##    num = int(input("Enter the numbers: "))
##    numbers.append(num)
##for num in numbers:
##    if num>=0:
##        positive.append(num)
##    else:
##        negative.append(num)
##print("Positive numbers: ", positive)
##print("Negative numbers: ", negative)

##numbers = [10, 20, 10, 30, 20, 40, 30]
##
##list = []
##
##for num in numbers:
##    if num not in list:
##        list.append(num)
##
##print(list)

##list1 = [10, 20, 30, 40]
##list2 = [30, 40, 50, 60]
##
##common = []
##
##for num in list1:
##    if num in list2:
##        common.append(num)
##
##print("Common elements:", common)
##


##numbers = [1, 2, 3, 5, 6]
##
##for i in range(1, 7):
##    if i not in numbers:
##        print("Missing number:", i)

numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)
