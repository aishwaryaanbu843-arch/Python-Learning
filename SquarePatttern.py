for i in range(6, 0, -1):
    for j in range(6-i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()
