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

def search_term_in_name(book:dict, search_term:str)->bool:
    result = False
    book_name:str = book["name"].strip().lower()
    if search_term.strip().lower() in book_name:
        result = True
    return result

def is_positive_int(number:int)->bool:
    result:bool = False
    if not isinstance(number,int) or isinstance(number,bool):
        return result
    if not number > 0:
        return result
    result = True
    return result

def is_author(book:dict, author:str)->bool:
    result = False
    book_author:str = book["author"].strip().lower()
    if author.strip().lower() == book_author:
        result = True
    return result

def is_title(book:dict, title:str)->bool:
    result = False
    book_title:str = book["name"].strip().lower()
    if title.strip().lower() == book_title:
        result = True
    return result

def is_book(book:dict,title:str,author:str)->bool:
    result = False
    if is_title(book,title) and is_author(book,author):
        result = True
        return result
    return result

def is_available(book:dict)->bool:
    result:bool = False
    availability:bool = book["available"]
    if availability == True:
        result = True
    return result

def is_book_id(book:dict,id:int)->bool:
    if not is_positive_int(id):
        return False
    book_id = book["id"]
    if id == book_id:
        return True
    return False 

def book_in_library(books:list[dict[str,str|int|bool]],title:str, author:str)->bool:
    result = False
    for book in books:
        if is_book(book,title,author):
            result = True
            return result
    return result

def id_in_library(books:list[dict[str,str|int|bool]],id:int)->bool:
    result = False
    for book in books:
        if is_book_id(book,id):
            result = True
            return result
    return result    
    