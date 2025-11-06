temp = int(input("Enter a temperature : "))
temp_state = input("Is the temperature in Celsius or Fahrenheit, Enter C for Celsius and F for fahrenheit: ")

if temp_state == "C":
    result = (temp - 32) * 5/9
    print(f"{temp} degrees celsius is {result} degrees fahrenheit")
elif temp_state == "F":
    result = (temp * 5/9) + 32
    print(f"{temp} degrees fahrenheit is {result} degrees celsius")
else:
    print("Invalid response")