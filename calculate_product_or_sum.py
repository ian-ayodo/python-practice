first_number = int(input("Enter a number : "))
second_number = int(input("Enter second number : "))

product = first_number * second_number
total = first_number + second_number
print(f"{first_number} + {second_number} = {total}" if product > 100 else f"{first_number} x {second_number} = {product}")