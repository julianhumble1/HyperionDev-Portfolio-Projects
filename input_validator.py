
valid_name = False      # sets up boolean for while loop

# while loop that takes user input of name and checks it is valid i.e. there are no numerical characters.
# while loop repeats until a valid name is entered.
while not valid_name:
    user_name = str(input("Please enter your first name: "))
    if user_name.isalpha():
        print("First name accepted.")
        valid_name = True
    else:
        print("Invalid first name. Please try again.")

# repeat of the above for surname this time.
valid_surname = False

while not valid_surname:
    user_surname = str(input("Please enter your surname: "))
    if user_surname.isalpha():
        print("Surname accepted.")
        valid_surname = True
    else:
        print("Invalid surname. Please try again.")

valid_phone = False

# while loop to confirm inputted phone number is in correct form.
while not valid_phone:
    user_phone = str(input("Please enter your phone number in the format 07XXX XXXXXX: "))
    # remove any spaces from user_phone to make more consistent and easy to work with
    stripped_number = user_phone.replace(" ", "")
    number_length = len(stripped_number)
    includes_letters = False
    wrong_start = False
    wrong_length = False

    # check that input only contains numerical digits. Print matching error message if not true.
    if not stripped_number.isdigit():
        print("Phone number can not include alphabetical or special characters. Please try again.")
        includes_letters = True
    # check that number begins with 07. Print matching error message if not true.
    if stripped_number[0:2] != "07":
        print("UK phone number must begin with '07'. Please try again.")
        wrong_start = True
    # check that exactly 11 digits have been entered. Print matching error message if not true.
    if number_length != 11:
        print("Phone number is the incorrect number of digits. Please enter a UK phone number in the format 07XXX XXXXXX. Please try again.")
        wrong_length = True


    # if no errors found above, accept phone number and break out of loop.
    if not (includes_letters or wrong_start or wrong_length):
        print("Phone number accepted.")
        valid_phone = True
    


    


