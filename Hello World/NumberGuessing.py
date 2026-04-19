import os
import random
import time

def menu():
    error = True
    while error:
        os.system("cls")
        print("------------------------------")
        print("1. Guess a number")
        print("2. I'll guess your number")
        print("3. Exit")
        print("------------------------------")

        try:
            menu_choice = int(input("Choose an option: "))
            if menu_choice == 1 or menu_choice == 2 or menu_choice == 3:
                error = False
            else:
                print("Please select a valid input\n")
                os.system("pause")
        except:
            print("Please select a valid input\n")
            os.system("pause")

    os.system("cls")
    return menu_choice

def game_1():
    random_num = random.randint(1, 100)
    guess_count = 0
    guessed_number = False
    
    print("I'm thinking of a random number betweeen 1 and 100...")
    time.sleep(1.5)
    print("I will tell you whether my number is higher or lower...")
    time.sleep(1.5)
    print("Good luck ;)")
    time.sleep(1.5)
    os.system("cls")

    guess = 0
    while not guessed_number:
        error = True
        while error:
            try:
                guess = int(input("Guess a number: "))
                if guess >= 1 and guess <= 100:
                    error = False
                else:
                    print("Please select a valid input\n")
            except:
                print("Please select a valid input\n")

        guess_count += 1
        if guess < random_num:
            print("Higher\n")
        elif guess > random_num:
            print("Lower\n")
        else:
            print("Yay! You guessed my number!")
            print("It took " + str(guess_count) + " attempts!")
            guessed_number = True
    
    print("")
    os.system("pause")

def game_2():
    guess_count = 0
    low_num = 1
    high_num = 100
    guess = 50
    higher_or_lower = ""
    last_guess = 0
    player_number = 0

    error = True
    while error:
        try:
            player_number = int(input("Choose a number between 1 and 100: "))
            if player_number >= 1 and player_number <= 100:
                error = False
            else:
                print("Please select a valid input\n")
        except:
            print("Please select a valid input\n")
    
    correct_guess = False
    while not correct_guess:
        print("Is your number " + str(guess) + "?")

        error = True
        false_input = True
        while error or false_input:
            try:
                higher_or_lower = input("Higher (h), Lower (l), Correct (c): ")
                print("")
                if higher_or_lower == "h" or higher_or_lower == "l" or higher_or_lower == "c":
                    error = False
                else:
                    print("Please select a valid input\n")
            except:
                print("Please select a valid input\n")
            
            if player_number > guess and higher_or_lower == "l":
                print("Don't lie to me! I know!\n")
            elif player_number < guess and higher_or_lower == "h":
                print("Don't lie to me! I know!\n")
            else:
                false_input = False
        
        if higher_or_lower == "c":
            print("Yay! It took me " + str(guess_count) + " attempts!")
            correct_guess = True
        elif guess == player_number:
            print("Why'd you lie? I win! It only took me " + str(guess_count) + " attempts!")
            correct_guess = True
        else:
            if higher_or_lower == "l":
                high_num = guess
            elif higher_or_lower == "h":
                low_num = guess

            guess_count += 1
            last_guess = guess
            guess = (high_num + low_num) // 2
            if last_guess == guess:
                guess += 1
    
    print("")
    os.system("pause")

if __name__ == "__main__":
    game = True
    while game:
        game_selector = menu()
        if game_selector == 1:
            game_1()
        elif game_selector == 2:
            game_2()
        elif game_selector == 3:
            game = False
            print("Thanks for playing! :)")
            time.sleep(1.5)
        os.system("cls")