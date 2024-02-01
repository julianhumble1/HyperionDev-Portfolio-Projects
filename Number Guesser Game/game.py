import random

from functions import *

user_info = "user_info.txt"
score_data = "score_data.txt"

username_password = read_file_to_dict(user_info)
score_dict = read_file_to_dict(score_data)

print_highlight("Welcome to the number guessing game!")

# ask user if they already have an account
valid_input = False
while valid_input == False:
    existing_account = input_highlight("Do you already have an account?\n"
                                    "\n1 - Yes"
                                    "\n2 - No, I need to make one.\n"
                                    "\nEnter either 1 or 2 here: ")
    if existing_account in ["1", "2"]:
        valid_input = True
    else:
        print("Invalid input. Please enter a digit 1 or 2.")

# existing account - ask for username and password until match
if existing_account == "1":
    logged_in = False
    while logged_in == False:
        username = input_highlight("Please enter your username: ")
        # ensure user can't log in using "Username" even though it is in dictionary as label
        if username == "Username":
            print("Username not in database. Please try again.")
        elif username in username_password.keys():
            password = input_highlight("Please enter your password: ")
            if password == username_password[username]:
                print("Username and password accepted.")
                print(f"Welcome Back {username}.")
                logged_in = True
            else:
                print("Password does not match username.")
        else:
            print("Username not in database. Please try again.")

# create new account - add new details to dictionary
elif existing_account == "2":
    print_highlight("Account Creation Screen")
    new_username = input_highlight("Please enter a username: ")
    new_password = input_highlight("Please enter a password: ")
    # add new username and password to username_password dictionary
    username_password[new_username] = new_password
    # add username and no high score to score data
    score_dict[new_username] = "No Hi-Score"
    print_highlight(f"Welcome {new_username}. Account Created Successfully.")
    username = new_username
    logged_in = True

save_dict(username_password, user_info)
save_dict(score_dict, score_data)

while logged_in:
    # Number Guesser Game
    print_highlight("Number Guesser")
    # initialise numbers for game
    target_number = random.randint(1,100)
    attempts = 0
    guess = 0
    lower_bound = 1
    upper_bound = 100
    while guess != target_number:
        valid_input = False
        while valid_input == False:
            try:
                guess = int(input_highlight(f"Enter your guess between {lower_bound} "
                                    f"and {upper_bound} here: "))
                valid_input = True
            except:
                print("Invalid input. Please choose an integer value.")
        if guess > target_number:
            print("Too high! Try again.")
            upper_bound = guess
        elif guess < target_number:
            print("Too low! Try again")
            lower_bound = guess
        attempts += 1

    # Guessed target number correctly so print congratulations
    print_highlight("Congratulations! You have found the target "
                    f"number {target_number}. You did this in "
                    f"{attempts} attempts.")
    
    # if they have not played before, sets score as their hi-score
    if score_dict[username] == "No Hi-Score":
        score_dict[username] = str(attempts)
    
    # failed to beat high score
    elif int(score_dict[username]) <= attempts:
        print("Unfortunately you didn't beat your high score of "
              f"{score_dict[username]} ")
        
    # beat hi-score, set new high score and save to dictionary
    elif int(score_dict[username]) > attempts:
        print("Congratulations! New Hi-Score!")
        score_dict[username] = str(attempts)

    print(f"Your Hi-Score: {score_dict[username]}")
    
    # ask if they want to play again or log out
    valid_input = False
    while valid_input == False:
        play_again = input_highlight("Do you want to play again?\n"
                                        "\n1 - Yes"
                                        "\n2 - No, log me out.\n"
                                        "\nEnter either 1 or 2 here: ")
        if play_again in ["1", "2"]:
            valid_input = True
        else:
            print("Invalid input. Please enter a digit 1 or 2.")
    if play_again == "2":
        logged_in = False

# save data back to txt files before logging out.
save_dict(username_password, user_info)
save_dict(score_dict, score_data)

print_highlight("You have successfully logged out.")
