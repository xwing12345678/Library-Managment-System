from validations import is_non_empty_string,book_in_library, get_non_empty_input
from books import books

def display_books(books:list[dict[str,str|int|bool]])->None:
    for book in books:
        print(book)

def get_input(message:str)->str:
    user_input = input(message)
    return user_input

def book_name_flow(books:list[dict[str,str|int|bool]]):
    message = "Enter a book name (partial names also work): "
    user_input = get_input(message)
    print( search_book(books,user_input))

def search_book(books:list[dict[str,str|int|bool]], name:str)->dict[str,str|int|bool]|list[dict[str,str|int|bool]]|None:
    if not is_non_empty_string(name):
        return None
    result_list:list = []
    first_result:dict = {}
    for book in books:
        if book_in_library(book,name):
            result_list.append(book)
            if not first_result:
                first_result = book
    if first_result:
        if len(result_list)>1:
            return result_list
        return first_result
    else:
        return None

def get_available_books(books:list[dict[str,str|int|bool]])->list[dict[str,str|int|bool]]:
    available_book_list:list[dict[str,str|int|bool]] = []
    for book in books:
        book_available = book["available"]
        if book_available:
            available_book_list.append(book)
    return available_book_list
  
