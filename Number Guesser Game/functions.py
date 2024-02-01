# move from "Username | Password\nJulian | Humble" (in text file)
# to {"Username":"Password, "Julian":"Humble"}
def read_file_to_dict(file_name):
    with open(file_name, "r") as data:
        data_list = []
        for line in data.readlines():
            split_line = line.split(" | ")
            stripped_line = [item.strip() for item in split_line]
            data_list.append(stripped_line)
        new_dict = {data_list[i][0]:data_list[i][1] for i in range(len(data_list))}
    return new_dict

# function to format dictionary data ready for save
def format_for_save(data_dict):
    # move from {"Username":"Password, "Julian":"Humble"}
    # to ["Username | Password", "Julian | Humble"]
    dict_to_list = [" | ".join(line) for line in data_dict.items()]
    # move from ["Username | Password", "Julian | Humble"]
    # to "Username | Password\nJulian | Humble"
    string_for_save = "\n".join(dict_to_list)
    return string_for_save

# function that saves a dictionary to a specified file name
def save_dict(data_dict, file_name):
    new_data_string = format_for_save(data_dict)
    with open(file_name, "w") as data:
        data.write(new_data_string)    

def print_highlight(menu_name):
    print("-" * 80)
    print(f"{menu_name}")
    print("-" * 80)

def input_highlight(input_prompt):
    print("-" * 80)
    output = input(f"{input_prompt}")
    print("-" * 80)
    return output