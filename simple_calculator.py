while True:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    calculation = input("S - Sum, Sub - Subtraction, M - Multiplication, D - Division, Q - Quit: ")
    result = 0

    if calculation.upper() == "S":
        result = first_number + second_number
        print(f"{first_number} + {second_number} = {result}")
    elif calculation.upper() == "Sub":
        result = first_number - second_number
        print(f"{first_number - second_number} = {result}")
    elif calculation.upper() == "M":
        result = first_number * second_number
        print(f"{first_number} * {second_number} = {result}")
    elif calculation.upper() == "D":
        try:
            result = first_number/second_number
            print(f"{first_number}/{second_number} = {result}")
        except ZeroDivisionError:
            print("You cannot divide by zero")
        except ValueError:
            print("Enter a valid number")
    elif calculation.upper() == "Q":
        break
    else:
        print("Enter a valid number")

