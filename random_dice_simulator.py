import  random

while True:
    roll_dice = input("Roll dice?(y/n) : ")
    if roll_dice.upper() == "Y":
        print(random.randint(1,6))
    elif roll_dice.upper() == "N":
        break
    else:
        print ("Enter a valid number")