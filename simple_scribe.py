
# program to be a document creater and editor, with headings and body text in different sizes.
# returns output to be copied into markdown file to produce formatted text.

# Formatting from Markdown File:
# - #TEXT - larger header
# - ###TEXT - smaller header
# - *TEXT* - italic
# - **TEXT** - bold
# - * TEXT - bullet point
# - | Left columns  | Right columns |
# - | ------------- |:-------------:|
# - | left foo      | right foo     |
# - | left bar      | right bar     |
# - | left baz      | right baz     |

# opening line to print
print("")
print("-"*80)
print("\n Welcome to the Python text-editor-o-matic! \n")            

return_output = []
finished_scribing = False

# define functions for string modification based on bold or italic

def bold(text): 
    bold_text = (f"**{text}**")
    return bold_text

def italic(text):
    italic_text = (f"*{text}*")
    return italic_text

while finished_scribing == False:

    # Main Menu 
    print("-"*80)
    print("\nMAIN MENU\n")
    print("Please select a choice from the list below:\n")
    print("1\t - Add Text")
    print("2\t - Edit Text")
    print("3\t - View Text")
    print("4\t - Finish scribing and return output\n")
    print("-"*80)

    main_user_choice = input("Please enter a choice from the menu above: ")
    print("-"*80)

    if main_user_choice == "1":         # Add Text
        # Add Text Menu
        print("\nADD TEXT MENU\n")
        print("1\t - Add Heading")
        print("2\t - Add Sub-Heading")
        print("3\t - Add Text to Main Body")
        print("4\t - Add Line Space (New Paragrah)", "\n")
        print("-"*80)
        add_user_choice = input("Please enter a choice from the menu above: ")
        print("-"*80)
        if add_user_choice == "1":
            # Font selection menu
            print("\nFONT CHOICE MENU\n")
            print("1\t Standard Font")
            print("2\t Italic")
            print("3\t Bold")
            print("")
            print("-"*80)
            font_option = input("Please enter a choice from the menu above: ")
            print("-"*80)
            # depending on font choice, prompts user to enter their heading
            if font_option == "1":
                new_heading = ("# " + input("Please write your heading here: ") + "\n")
                return_output.append(new_heading)
            elif font_option == "2":
                new_heading = ("# " + italic(input("Please write your heading here: ")) + "\n")
                return_output.append(new_heading)
            elif font_option == "3":
                new_heading = ("# " + bold(input("Please write your heading here: ")) + "\n")
                return_output.append(new_heading)
            print("Heading added successfully.")
        if add_user_choice == "2":
            # Font selection menu
            print("\nFONT CHOICE MENU\n")
            print("1\t Standard Font")
            print("2\t Italic")
            print("3\t Bold")
            print("")
            print("-"*80)
            font_option = input("Please enter a choice from the menu above: ")
            print("-"*80)
            # depending on font choice, prompts user to enter their sub heading
            if font_option == "1":
                new_sub_heading = ("### " + input("Please write your sub-heading here: ") + "\n")
                return_output.append(new_sub_heading)
            elif font_option == "2":
                new_sub_heading = ("### " + italic(input("Please write your sub-heading here: ")) + "\n")
                return_output.append(new_sub_heading)
            elif font_option == "3":
                new_sub_heading = ("### " + bold(input("Please write your sub-heading here: ")) + "\n")
                return_output.append(new_sub_heading)
            print("Sub - Heading added successfully.")
        if add_user_choice == "3":
            # Font selection menu
            print("\nFONT CHOICE MENU\n")
            print("1\t Standard Font")
            print("2\t Italic")
            print("3\t Bold")
            print("")
            print("-"*80)
            font_option = input("Please enter a choice from the menu above: ")
            print("-"*80)
             # depending on font choice, prompts user to enter their main body text
            if font_option == "1":
                new_body_text = (input("Please enter your text here: ") + "\n")
                return_output.append(new_body_text)
            elif font_option == "2":
                new_body_text = (italic(input("Please enter your text here: ")) + "\n")
                return_output.append(new_body_text)
            elif font_option == "3":
                new_body_text = (bold(input("Please enter your text here: ")) + "\n")
                return_output.append(new_body_text)
            print("Text added successfully.")
        if add_user_choice == "4":
            # no font selection screen as just printing a new line.
            return_output.append("<br>\n")
            print("Line space inserted successfully.")
        
    if main_user_choice == "2":         # Edit Text
        # Edit Text Menu
        print("Which section of the text would you like to remove/replace?\n")
        # print each line of the output with a number next to it for the user to refer to
        for count, text in enumerate(return_output):
            print(count + 1, text)
        print("-"*80)
        edit_user_choice = int(input("Please enter a number corresponding with the section you would like to replace or remove: ")) - 1
        print("-"*80)
        print(f"\nHighlighted section:\n{return_output[edit_user_choice]}")
        print("-"*80)
        print("Would you like to replace or remove this section of text?\n")
        print("1-\t REPLACE this section of text.")
        print("2-\t REMOVE this section of text.")
        print("")
        print("-"*80)
        rep_or_rem = input("Please enter a choice from the menu above: ")
        print("-"*80)
        if rep_or_rem == "1":
            # Moves user into similar menu as above (Add text menu) but replacing return_output element rather than appending to the end.
            # Add Text Menu
            print("\nREPLACE TEXT MENU\n")
            print("1\t - Replace with Heading")
            print("2\t - Replace with Sub-Heading")
            print("3\t - Replace with Text to Main Body")
            print("4\t - Replace with Line Space (New Paragrah)", "\n")
            print("-"*80)
            add_user_choice = input("Please enter a choice from the menu above: ")
            print("-"*80)
            if add_user_choice == "1":
                # Font selection menu
                print("\nFONT CHOICE MENU\n")
                print("1\t Standard Font")
                print("2\t Italic")
                print("3\t Bold")
                print("")
                print("-"*80)
                font_option = input("Please enter a choice from the menu above: ")
                print("-"*80)
                # depending on font choice, prompts user to enter their heading
                if font_option == "1":
                    new_heading = ("# " + input("Please write your heading here: ") + "\n")
                    return_output[edit_user_choice] = new_heading
                elif font_option == "2":
                    new_heading = ("# " + italic(input("Please write your heading here: ")) + "\n")
                    return_output[edit_user_choice] = new_heading
                elif font_option == "3":
                    new_heading = ("# " + bold(input("Please write your heading here: ")) + "\n")
                    return_output[edit_user_choice] = new_heading
                print("Heading added successfully.")
            if add_user_choice == "2":
                # Font selection menu
                print("\nFONT CHOICE MENU\n")
                print("1\t Standard Font")
                print("2\t Italic")
                print("3\t Bold")
                print("")
                print("-"*80)
                font_option = input("Please enter a choice from the menu above: ")
                print("-"*80)
                # depending on font choice, prompts user to enter their sub heading
                if font_option == "1":
                    new_sub_heading = ("### " + input("Please write your sub-heading here: ") + "\n")
                    return_output[edit_user_choice] = new_sub_heading
                elif font_option == "2":
                    new_sub_heading = ("### " + italic(input("Please write your sub-heading here: ")) + "\n")
                    return_output[edit_user_choice] = new_sub_heading
                elif font_option == "3":
                    new_sub_heading = ("### " + bold(input("Please write your sub-heading here: ")) + "\n")
                    return_output[edit_user_choice] = new_sub_heading
                print("Sub - Heading added successfully.")
            if add_user_choice == "3":
                # Font selection menu
                print("\nFONT CHOICE MENU\n")
                print("1\t Standard Font")
                print("2\t Italic")
                print("3\t Bold")
                print("")
                print("-"*80)
                font_option = input("Please enter a choice from the menu above: ")
                print("-"*80)
                    # depending on font choice, prompts user to enter their main body text
                if font_option == "1":
                    new_body_text = (input("Please enter your text here: ") + "\n")
                    return_output[edit_user_choice] = new_body_text
                elif font_option == "2":
                    new_body_text = (italic(input("Please enter your text here: ")) + "\n")
                    return_output[edit_user_choice] = new_body_text
                elif font_option == "3":
                    new_body_text = (bold(input("Please enter your text here: ")) + "\n")
                    return_output[edit_user_choice] = new_body_text
                print("Text added successfully.")
            if add_user_choice == "4":
                # no font selection screen as just printing a new line.
                return_output[edit_user_choice] = "<br>\n"
                print("Line space inserted successfully.")

    if main_user_choice == "3":         # View Text
        for output_string in return_output:
            print(output_string)
    
    if main_user_choice == "4":         # Finish Scribing
        finished_scribing = True


# once out of while loop, print full text ready for pasting into markdown file
print("-"*80)
print("Please copy and paste the full below text into your markdown file.")
print("-"*80)
for output_string in return_output:
    print(output_string)
