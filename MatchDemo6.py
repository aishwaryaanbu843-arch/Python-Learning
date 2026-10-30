n = int(input("Enter a number: "))

factorial = 1

for i in range(n, 0, -1):
    factorial = factorial * i

print("Factorial =", factorial)
