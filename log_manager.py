# program to read in, edit and format shipment logs

# reads data from text file log_data.txt
# format data to be in one large list. Each entry in the list is of the form:
# ['01/01/2023 14:30', 'Shipment Received', '123001', 'New York', 'Electronics']
def read_from_txt():
    data_list = []
    with open(file_path, "r") as data:
        for log_line in data.readlines():
            split_line = log_line.split("|")
            stripped_line = [item.strip() for item in split_line]
            data_list.append(stripped_line)
    return data_list

# function that takes list of data logs and saves it to log.data.txt
# then reads file text back into list of strings ready for use.
def save_data(data_for_save):
    formatted_data = [" | ".join(log_line) for log_line in data_for_save]
    new_data_string = "\n".join(formatted_data)
    with open(file_path, "w") as data:
        data.write(new_data_string)
    new_data_list = read_from_txt()
    return new_data_list

# read in log_data.txt ready for use
file_path = "log_data.txt"
data_list = read_from_txt()

# define function that will output any log to the user in the desired format.
def print_log(log):
    date_time = log[0]
    log_type = log[1]
    log_ref = log[2]
    location = log[3]
    goods_type = log[4]
    log_output = f"\nDate: {date_time}\nActivity: {log_type}\nRef Number: "\
                + f"{log_ref}\nLocation: {location}\nGoods Type: {goods_type}\n"
    print(log_output)

# define function that prints result in easy to read way
def print_highlight(menu_name):
    print("-" * 80)
    print(f"{menu_name}")
    print("-" * 80)

# check date is in one of either YYYY or DD/MM/YYYY format
# returns boolean
def valid_date_check(date):
    if len(date) == 10 and (date[2] and date[5]) == "/" or \
        len(date) == 4 and date.isdigit():
        valid_date = True
    else:
        valid_date = False
    return valid_date

# check whether date is in format YYYY or DD/MM/YYYY
# returns long_format or year_only
def date_type_check(date):
    if len(date) == 10 and (date[2] and date[5]) == "/":
        date_type = "long_format"
    elif len(date) == 4 and date.isdigit():
        date_type = "year_only"
    return date_type

# check type entered is one of dispatched, delivered or received
# returns boolean
def valid_type_check(type):
    if type.lower() in ["shipment dispatched", "shipment delivered", "shipment received"]:
        valid_type = True
    else:
        valid_type = False
    return valid_type

# check ref entered is 6 numerical digits
# returns boolean
def valid_ref_check(ref):
    if len(ref.strip()) == 6 and ref.isdigit():
        valid_ref = True
    else:
        valid_ref = False
    return valid_ref

# check location entered is only alphabetical
# returns boolean
def valid_location_check(location):
    if location.isalpha():
        valid_location = True
    else:
        valid_location = False
    return valid_location

# check goods entered is only alphabetical
# returns boolean
def valid_goods_check(goods):
    if goods.isalpha():
        valid_goods = True
    else:
        valid_goods = False
    return valid_goods

# define function that asks user for date to search by , prints and returns
# all results with that date to search_results
# parameter show_count True or False:
# if True then displays count of each result to user for reference.
def search_by_date(show_count):
    print_highlight("Date Filter Selected")
    print(("Please enter a date in the format DD/MM/YYYY, "
            "or a year in the format YYYY"))
    valid_input = False
    # use while loop to keep requesting input until valid date entered.
    while valid_input == False:
        date_filter = input("Please enter a date: ")
        # if they have entered a year YYYY:
        search_results = []
        if valid_date_check(date_filter):
            if date_type_check(date_filter) == "year_only":
                print_highlight(f"Found all entries from the year entered:"
                                f"({date_filter})")
                if show_count == True:
                    result_number = 1
                    for log_line in data_list:
                        if date_filter in log_line[0]:
                            print(f"Result {result_number}:")
                            print_log(log_line)
                            print("")
                            result_number += 1
                            search_results.append(log_line)
                else:
                    for log_line in data_list:
                        if date_filter in log_line[0]:
                            print_log(log_line)
                            print("")
            else:
                print_highlight(f"Found all entries from the date entered:"
                                f"({date_filter})")
                if show_count == True:
                    result_number = 1
                    for log_line in data_list:
                        if date_filter in log_line[0]:
                            print(f"Result {result_number}:")
                            print_log(log_line)
                            print("")
                            result_number += 1
                            search_results.append(log_line)
                else:
                    for log_line in data_list:
                        if date_filter in log_line[0]:
                            print_log(log_line)
                            print("")
            valid_input = True
        else:
            print("Invalid date inputted. Please enter a date "
                    "in the format DD/MM/YYYY or a year in the format YYYY.")
            
    return search_results

# same as function defined above for activity type rather than date
def search_by_type(show_count):
    print_highlight("Activity Type Filter Selected")
    valid_input = False
    # use while loop to keep requesting input until valid date entered.
    while valid_input == False:
        print(("Please enter one of the following:"
                "\nShipment Dispatched"
                "\nShipment Delivered"
                "\nShipment Received"))
        type_filter = input("Please enter one of the above options: ")
        if valid_type_check(type_filter):
            search_results = []        
            print_highlight(f"Found all entries for log type {type_filter}:")
            if show_count == True:
                result_number = 1
                for log_line in data_list:
                    if type_filter == log_line[1]:
                        print(f"Result {result_number}:")
                        print_log(log_line)
                        print("")
                        result_number += 1
                        search_results.append(log_line)
            else:
                for log_line in data_list:
                    if type_filter == log_line[1]:
                        print_log(log_line)
                        print("")
                    search_results.append(log_line)
            valid_input = True
        else:
            print("Invalid entry. Please try again.")
            print(("Please enter one of the following:"
                "\nShipment Dispatched"
                "\nShipment Delivered"
                "\nShipment Received"))       
    return search_results

# define function to search by log ref number.
# no show_count parameter as there should always be one result (unique ref numbers)
def search_by_ref():
    print_highlight("Log Ref Filter Selected")
    valid_input = False
    while valid_input == False:
        ref_filter = input("Please enter a 6-digit reference number to search: ")
        search_results = []
        if valid_ref_check(ref_filter):
            print_highlight(f"Found log entry for the ref {ref_filter}:")
            for log_line in data_list:
                if ref_filter in log_line[2]:
                    print_log(log_line)
                    print("")
                    search_results.append(log_line)
            valid_input = True
        else:
            print("You must enter a 6-digit number. Please try again.")
    return search_results

# define function to search by location.
# parameter show_count True or False:
# if True then displays count of each result to user for reference.
def search_by_location(show_count):
    print_highlight("Location Filter Selected")
    valid_input = False
    while valid_input == False:
        loc_filter = input("Please enter a location to filter by: ")
        search_results = []
        if valid_location_check(loc_filter):
            print_highlight(f"Found all entries for {loc_filter}:")
            if show_count == True:
                result_number = 1
                for log_line in data_list:
                    if loc_filter in log_line[3]:
                        print(f"Result {result_number}:")
                        print_log(log_line)
                        print("")
                        result_number += 1
                        search_results.append(log_line)
            else:
                for log_line in data_list:
                    if loc_filter in log_line[3]:
                        print_log(log_line)
                        print("")
                        search_results.append(log_line)
            valid_input = True
        else:
            print("No numerical or special characters allowed. "
                    "Please try again.")
    return search_results

# define function to search by goods type.
# parameter show_count True or False:
# if True then displays count of each result to user for reference.
def search_by_goods(show_count):
    print_highlight("Goods Type Menu")
    valid_input = False
    while valid_input == False:
        goods_filter = input("Please enter a type of good to filter by: ")
        search_results = []
        if valid_goods_check:
            print_highlight(f"Found all entries for {goods_filter}:")
            if show_count == True:
                result_number = 1
                for log_line in data_list:
                    if goods_filter in log_line[4]:
                        print(f"Result {result_number}:")
                        print_log(log_line)
                        print("")
                        result_number += 1
                        search_results.append(log_line)
            else:
                for log_line in data_list:
                    if goods_filter in log_line[4]:
                        print_log(log_line)
                        print("")
                        search_results.append(log_line)
            valid_input = True
        else:
            print("No numerical or special characters allowed. "
                    "Please try again.")
    return search_results

# while loop to enter interactive menu
log_out = False
while log_out == False:
    # Print Main Menu for user to select from
    print_highlight("Main Menu")
    print("Please select an option from the menu below:"
        "\n1 - View Log Data"
        "\n2 - Edit Existing Log Data"
        "\n3 - Add New Log"
        "\n4 - Save all changes and Log Out")
    user_choice = input("Please enter a number 1-4: ")

    # View Log Data
    if user_choice == "1":
        # Filter Choice Menu
        print_highlight("Filter Choice Menu")
        print("Select Filter For Data Log: "
            "\n1 - Date"
            "\n2 - Log Type"
            "\n3 - Log Ref Number"
            "\n4 - Warehouse Location"
            "\n5 - Goods Type")
        filter_choice = input("Please enter a number 1-5: ")

        # Date Filter Menu
        if filter_choice == "1":
            search_by_date(False)

        # Type Filter Menu
        elif filter_choice == "2":
            search_by_type(False)

        # Log Ref Menu
        elif filter_choice == "3":
            search_by_ref()

        # Location Menu
        elif filter_choice == "4":
            search_by_location(False)
                    
        # Goods Type Menu
        elif filter_choice == "5":
            search_by_goods(False)

    # Edit Log Data
    elif user_choice == "2":
        print_highlight("Select Filter For Data Log Search or return to Main Menu: ")
        print("1 - Date"
            "\n2 - Log Type"
            "\n3 - Log Ref Number"
            "\n4 - Warehouse Location"
            "\n5 - Goods Type"
            "\n6 - Return to Main Menu")
        filter_choice = input("Please enter a number 1-6: ")

        # Return to Main Menu
        if filter_choice == "6":
            continue

        # Date Filter Menu
        elif filter_choice == "1":
            search_results = search_by_date(True)
        
        # Type Filter Menu
        elif filter_choice == "2":
            search_results = search_by_type(True)

        # Log Ref Menu
        elif filter_choice == "3":
            search_results = search_by_ref()

        # Location Menu
        elif filter_choice == "4":
            search_results = search_by_location(True)
                    
        # Goods Type Menu
        elif filter_choice == "5":
            search_results = search_by_goods(True)

        # takes search_results and confirms with user which log to edit
        total_results = len(search_results)
        if total_results >= 1:
            if total_results > 1:
                print_highlight(f"Select a result from the list "
                                f"above using a digit 1 - {total_results}")
                edit_choice = int(input(f"Enter digit between 1 "
                                    f"and {total_results}: "))
            elif total_results == 1:
                print_highlight("Only one result. Proceeding to edit.")
                edit_choice = 1
            log_for_edit = search_results[edit_choice - 1]
        else:
            print_highlight("No results found, returning to main menu.")
            continue

        finished_editing = False
        while finished_editing == False:
            print_highlight("This is the log selected for edit: ")
            print_log(log_for_edit)
            print_highlight("All changes are temporary until saved.\n"
                            "Please select an element of this log to change"
                            "or Return to Main Menu:")
            print("1 - Date"
            "\n2 - Log Type"
            "\n3 - Log Ref Number"
            "\n4 - Warehouse Location"
            "\n5 - Goods Type"
            "\n6 - Return to Main Menu")
            edit_element = input("Please enter a number 1-6: ")

            # check they have entered a valid input
            if edit_element not in ["1", "2", "3", "4", "5", "6"]:
                print("Invalid entry. Please enter a digit 1-6.")

            # SAVE and return to Main Menu
            if edit_element == "6":
                finished_editing = True

            # change the chosen log DATE
            elif edit_element == "1":
                new_value = input("Please enter a new value: ")
                # check new date is in correct format
                if valid_date_check(new_value):
                    if date_type_check(new_value) == "long_format":
                        # find log entry with same log ref and replaces date with new value.
                        for ref_check in data_list:
                            if log_for_edit[2] == ref_check[2]:
                                print_highlight(f"Old Date Value: {ref_check[0]}\n"
                                                f"New Date Value: {new_value}")
                                ref_check[0] = new_value
                    else:
                        print("Invalid date format. Please enter DD/MM/YYYY.")
                else:
                    print("Invalid date format. Please enter DD/MM/YYYY.")

            # change the chosen log TYPE
            elif edit_element == "2":
                new_value = input("Please enter a new value: ")
                if valid_type_check(new_value):
                    for ref_check in data_list:
                        if log_for_edit[2] == ref_check[2]:
                            print_highlight(f"Old Log Type: {ref_check[1]}\n"
                                            f"New Log Type: {new_value}")
                            ref_check[1] = new_value
                else:
                    print("Invalid Entry. Please enter Shipment Dispatch, Shipment "
                        "Delivered or Shipment Received")
            
            # change the chosen log REF
            elif edit_element == "3":
                new_value = input("Please enter a new six- digit value: ")
                if valid_ref_check(new_value):
                    for ref_check in data_list:
                        if log_for_edit[2] == ref_check[2]:
                            print_highlight(f"Old Log Ref: {ref_check[2]}\n"
                                            f"New Log Ref: {new_value}")
                            ref_check[2] = new_value
                else:
                    print("Invalid Entry. New log ref number must be 6 numerical digits.")

            # change the chosen log LOCATION
            elif edit_element == "4":
                new_value = input("Please enter a new value: ")
                if valid_location_check(new_value):
                    for ref_check in data_list:
                        if log_for_edit[2] == ref_check[2]:
                            print_highlight(f"Old Location: {ref_check[3]}\n"
                                            f"New Location: {new_value}")
                            ref_check[3] = new_value
                else:
                    print("Invalid Entry. New location must be alphabetic characters only.")

            # change the chosen log GOODS TYPE
            elif edit_element == "5":
                new_value = input("Please enter a new value: ")
                if valid_goods_check(new_value):
                    for ref_check in data_list:
                        if log_for_edit[2] == ref_check[2]:
                            print_highlight(f"Old Location: {ref_check[4]}\n"
                                            f"New Location: {new_value}")
                            ref_check[4] = new_value
                else:
                    print("Invalid Entry. New location must be alphabetic characters.")

    # Add New Log        
    elif user_choice == "3":
        finished_adding = False
        print_highlight("New Log Entry Selected")
        while finished_adding == False:

            print_highlight("Please enter details of new log")

            # Enter DATE for new log
            valid_date = False
            while valid_date == False:
                new_date = input("Please enter new date here in DD/MM/YYYY format: ")
                if valid_date_check(new_date) == True:
                    if date_type_check(new_date) == "long_format":
                        print_highlight("New Date Accepted.")
                        valid_date = True
                    else:
                        print_highlight("Invalid entry. Please enter date in DD/MM/YYYY format.")
                else:
                    print_highlight("Invalid entry. Please enter date in DD/MM/YYYY format.")
            
            # Enter TYPE for new log
            valid_type = False
            while valid_type == False:
                print("Please enter one of the following new activity types:"
                        "\nShipment Dispatched"
                        "\nShipment Delivered"
                        "\nShipment Received")
                new_type = input("Please enter new activity type: ")
                if valid_type_check(new_type):
                    print_highlight("New Actvity Type Accepted.")
                    valid_type = True
                else:
                    print_highlight("Invalid entry. Please try again.")

            # Enter REF for new log
            valid_ref = False
            while valid_ref == False:
                new_ref = input("Please enter a new six- digit value log reference number: ")
                if valid_ref_check(new_ref):
                    print_highlight("New Log Ref Accepted")
                    valid_ref = True
                else:
                    print_highlight("Invalid Entry. New log ref number must be 6 numerical digits.")

            # Enter LOCATION for new log
            valid_location = False
            while valid_location == False:
                new_location = input("Please enter a location for the new log: ")
                if valid_location_check(new_location):
                    print_highlight("New Location Accepted")
                    valid_location = True
                else:
                    print_highlight("Invalid Entry. New location must be alphabetic characters only.")

            # Enter GOODS TYPE for new log
            valid_goods = False
            while valid_goods == False:
                new_goods = input("Please enter a goods type for the new log: ")
                if valid_goods_check(new_goods):
                    print_highlight("New Location Accepted")
                    valid_goods = True
                else:
                    print_highlight("Invalid Entry. New goods type must be alphabetic characters only.")


            # shows user new log details and confirms they are happy to add
            new_log = [new_date, new_type, new_ref, new_location, new_goods]
            print_highlight("New Log Shown Below. Please confirm it is correct before proceeding.")
            print_log(new_log)
            print("")
            valid_correct_log = False
            while valid_correct_log == False:
                print("1 - All correct, please add to log"
                      "\n2 - Re-Enter new log details\n")
                correct_log = input("Please enter 1 or 2: ")
                if correct_log == "1":
                    data_list.append(new_log)
                    print_highlight("New Log Successfully Added.")
                    # confirm if user wants to add another log or return to main menu
                    print_highlight("Would you like to add another log or return to Main Menu?")
                    valid_input = False
                    while valid_input == False:
                        print("1 - Add Another Log"
                        "\n2 - Save Changes and Return to Main Menu\n")
                        new_log_or_menu = input("Please enter 1 or 2: ")
                        if new_log_or_menu == "1":
                            valid_input = True
                        elif new_log_or_menu == "2":
                            finished_adding = True
                            valid_input = True
                        else:
                            print("\nPlease enter a digit 1 or 2.")
                    valid_correct_log = True
                elif correct_log == "2":
                    print_highlight("Please re-enter details.")
                    valid_correct_log = True
                else:
                    print("Please enter a digit 1 or 2.")
            
    # SAVE and log out
    elif user_choice == "4":
        save_data(data_list)
        print_highlight("You have successfully saved and logged out.")
        log_out = True
