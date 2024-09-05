import random
answer = random.randint(0,49)

def easymode():
    print("Please Guess a number below 50")
    try:
        guess = int(input("> "))

        if guess == answer:
            print("!!!Congrats. You have won")
        elif guess > answer:
            print("You have a higher value than actual answer.")
            easymode()
        elif guess < answer:
            print("You have a lower value than actual answer.")
            easymode()

    except ValueError:
        print("Please enter a number.")

def hardmode():
    print("Please Guess a number below 50")

    tries = 0

    while tries < 5:
        try:
            guess = int(input("> "))

            if guess == answer:
                print("!!!Congrats. You have won")
                break

            elif guess > answer:
                print("You have a higher value than actual answer.")
                tries += 1
                if tries == 5:
                    print(f"You have failed at guessing the correct number. You used all your {tries} tries.") 
                    print(f"The correct answer was: {answer}")
                else:
                    print(f"Try again. You have {5 - tries} tries left.")
            elif guess < answer:
                print("You have a lower value than actual answer.")
                tries += 1
                if tries == 5:
                    print(f"You have failed at guessing the correct number. You have {tries} tries.")
                else:
                    print(f"Try again. You have {5 - tries} tries left")

        except ValueError:
            print("Please enter a number.")

def pregame():
    print("Select the mode. \n 1.Easy 2.Hard 3.Help")
    try:
        choice = int(input("Enter the choice: "))

        if choice == 1:
            print("EASY MODE")
            easymode()
        elif choice == 2:
            print("HARD MODE")
            hardmode()
        elif choice == 3:
            print("HELP")
            print("In Easy mode you have unlimited tries. \nBut in Hard mode yoy have only 5 tries")
        else:
            print("Invalid Choice")
            pregame()

    except ValueError:
        print("Enter your choice")

pregame()
