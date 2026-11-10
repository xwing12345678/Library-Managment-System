from books import books
valid_menu_choices:list[str] = [str(integer) for integer in range(1,9)]


def is_non_empty_string(raw_string:str)->bool:
    result:bool = False
    if raw_string.strip():
        result = True
    return result

def get_valid_menu_choice(message:str,valid_choices:list)->str:
    user_input:str = ""
    valid_choice = False
    while valid_choice == False:
        user_input = get_non_empty_input(message)
        if user_input not in valid_choices:
            print('Your input is not in the provided list!',
                   'Enter in a valid choice from the list!')
            continue
        valid_choice = True
        break
    return user_input

def get_non_empty_input(message:str)->str:
    non_empty_choice = False
    user_input:str = ""
    while non_empty_choice == False:
        user_input = input(message)
        if not is_non_empty_string(user_input):
            print("You must enter an actual choice!",
            'Just spaces or pressing enter are not valid!')
            continue
        non_empty_choice = True
    return user_input

def book_in_library(book:dict, search_term:str)->bool:
    result = False
    book_name:str = book["name"].strip().lower()
    if search_term.strip().lower() in book_name:
        result = True
    return result

