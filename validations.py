
def is_non_empty_string(raw_string:str)->bool:
    result:bool = False
    if raw_string.strip():
        result = True
    return result

def get_valid_menu_choice(message:str,valid_choices:list)->str:
    valid_choice = False
    user_input:str = ""
    while valid_choice == False:
        user_input = input(message)
        if not is_non_empty_string(user_input):
            print("You must enter an input from the list!")
            continue
        if user_input not in valid_choices:
            print('Your input is not in the provided list!',
                   'Enter in a valid choice from the list!')
            continue
        valid_choice = True
        break
    return user_input

