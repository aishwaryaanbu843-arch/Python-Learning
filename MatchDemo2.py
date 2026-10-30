print("CHOOSE THE FOOD YOU WOULD LIKE TO HAVE:\n 1 -> Pizza\n 2 -> Burger\n 3 -> Pasta\n 4 -> Sandwich ")
eat = input("Enter your choice: ")
match eat:
    case "Pizza":
        print("It costs 200 rupess")
    case "Burger":
        print("It costs 120 rupees")
    case "Pasta":
        print("It costs 150 rupees")
    case "Sandwich":
        print("It costs 100 rupees")
    case _:
        print("Nothing")

