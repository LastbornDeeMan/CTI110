# CTI - 110
# P5HW1 - Math Quiz
# Davisc
# 11/12/23

import random

def generate_numbers():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    return num1, num2

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def display_menu():
    print("MENU")
    print("1. Add numbers")
    print("2. Subtract numbers")
    print("3. Quit")

def main():
    choice = 0
    while choice != 3:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            num1, num2 = generate_numbers()
            total = add_numbers(num1, num2)
            guess = int(input(f"What is {num1} + {num2}? "))
            if guess == total:
                print("Congratulations! You guessed it right!")
            else:
                print(f"Sorry, the correct answer is {total}")
        elif choice == 2:
            num1, num2 = generate_numbers()
            result = subtract_numbers(num1, num2)
            guess = int(input(f"What is {num1} - {num2}? "))
            if guess == result:
                print("Congratulations! You guessed it right!")
            else:
                print(f"Sorry, the correct answer is {result}")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()