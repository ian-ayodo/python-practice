import random

def play_game():
    random_number = random.randint(0, 100)
    while True:
        try:
            guess = int(input("Guess my number (0–100): "))
            if guess > random_number:
                print(f"You’re {guess - random_number} too high. Try again.")
            elif guess < random_number:
                print(f"You’re {random_number - guess} too low. Try again.")
            else:
                print(f"🎉 Correct! My number was {random_number}.")
                break
        except ValueError:
            print("Please enter a valid number.")

while True:
    choice = input("Do you want to play? (Y/N): ").strip().upper()
    if choice == "Y":
        play_game()
    elif choice == "N":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter Y or N.")
