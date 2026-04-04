import time
import random

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def start_game():
    slow_print("🌃 Welcome to CITY ESCAPE")
    name = input("Enter your name: ")
    slow_print(f"\nAlright {name}, you're alone in a dangerous city at night...")
    slow_print("Your goal: Survive and find a way out.\n")
    
    main_street()

def main_street():
    slow_print("You are standing on a dimly lit street.")
    slow_print("Where do you want to go?")
    slow_print("1. Enter a cafe ☕")
    slow_print("2. Walk into a dark alley 🌑")
    slow_print("3. Go to the subway 🚇")

    choice = input("Choose (1/2/3): ")

    if choice == "1":
        cafe()
    elif choice == "2":
        alley()
    elif choice == "3":
        subway()
    else:
        slow_print("Invalid choice. Try again.\n")
        main_street()

def cafe():
    slow_print("\nYou enter a quiet cafe.")
    
    event = random.choice(["safe", "thief"])

    if event == "safe":
        slow_print("You found food and regained energy.")
        slow_print("A backdoor leads you out safely. You escaped! 🎉")
    else:
        slow_print("A thief was hiding inside!")
        slow_print("You got robbed. Game Over.")

def alley():
    slow_print("\nYou walk into the dark alley...")
    
    event = random.choice(["escape", "danger"])

    if event == "escape":
        slow_print("You found a shortcut out of the city!")
        slow_print("You escaped safely! 🎉")
    else:
        slow_print("A gang surrounds you.")
        slow_print("You couldn't escape. Game Over.")

def subway():
    slow_print("\nYou enter the subway station.")
    slow_print("It's empty... too empty.")
    
    slow_print("Do you want to:")
    slow_print("1. Take the train")
    slow_print("2. Go back")

    choice = input("Choose (1/2): ")

    if choice == "1":
        slow_print("The train starts moving...")
        slow_print("It takes you out of the city. You escaped! 🎉")
    else:
        main_street()

if __name__ == "__main__":
    start_game()
