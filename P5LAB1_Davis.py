# CTI 110
# P5LAB1 - CYOA
# name
# date
# Feel free to fork this REPL and make changes.

# first function: main_menu().

def main_menu():
    print("Main Menu")
    print("You're in front of a spooky old house...")
    print("Do you:")
    print("1. Try the front door")
    print("2. Sneak around back")
    print("3. Forget it and go home")
    print("4. [Quit]")
    choice = input("Choose: ")
    if choice == '1':
        choice_front_door()
    elif choice == '2':
        choice_back_door()
        pass
    elif choice == '3':
        choice_go_home()
        pass
    elif choice == '4':
        print("Ok, quitting game")
        return
    else:
        print("That's not a valid choice, please try again.")
        main_menu()

# now we have the choice functions. Feel free to add more.
def choice_front_door():
    print("Try the front door.")
    print("It's locked.")
    print("Do you:")
    print("1. Check around back")
    print("2. Give up and go home")
    choice = input("Choose: ")
    if choice == '1':
        choice_back_door()
    elif choice == '2':
        choice_go_home()
    else:
        print("You have to choose...")
        choice_front_door()

def choice_back_door():
    print("Machine, turn back now. The layers of this palace are not for your kind. Turn back, or you will be crossing the Will of GOD...")

def choice_go_home():
    print("it followed me home Cesar")

# finally, we have main -- which we use to start the program 
def main():
    print("M5LAB1 - Choose Your Own Adventure")
    main_menu()
    print("Thanks for playing!")

#start the program
main()
