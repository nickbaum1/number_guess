import random

def number_game():
    current_number = random.randint(-100, 100)
    print("This is a number guessing game.")
    print("Guess what number I have thought of between -100 to 100.")
    print("You will get 5 chances with hints.")
    user_input = input("Enter your guess: ")
    try:
        value = int(user_input)
        if -100 < value < 100:
            chances = 4
            while chances != 0:
                print(current_number)
                if int(user_input) < current_number:
                    print("Your guess is less than the number.")
                    chances = chances - 1
                    user_input = input("Enter your guess: ")
                elif int(user_input) > current_number:
                    print("Your guess is greater than the number.")
                    chances = chances - 1
                    user_input = input("Enter your guess: ")
                else:
                    print("Congratulations, your guess was correct. Restart to play again.")
                    quit()
            if chances == 0:
                print("You have failed. Restart to try again.")
                quit()
        else:
            print("Error: Number is not within predetermined range")
    except ValueError:
        try:
            value = float(user_input)
            print("Error: Number input must be an integer")
        except ValueError:
            print("Error: Input is not a number")

number_game()
