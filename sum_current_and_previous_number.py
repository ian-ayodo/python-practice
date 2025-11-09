numbers = list(range(10))
previous = 0

print("Printing current and previous numbers in a range (10)")

for number in numbers:
    total = number + previous
    print(f"Current Number {number} Previous Number {previous} Sum: {total}")
    previous = number
