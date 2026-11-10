from books import books
from get_books import get_input
from validations import is_non_empty_string, is_positive_int,book_in_library

def get_next_book_id(books:list[dict[str,str|int|bool]] )->int:
    unique_id = False
    next_id:int = 1
    if books:
        next_id += len(books)
    while not unique_id:
        for book in books:
            if book['id'] == next_id:
                next_id+=1
                continue
        unique_id = True
    return next_id

def borrow_book(books:list[dict[str,str|int|bool]] , book_id:int)->bool:
    
    

def return_book(books:list[dict[str,str|int|bool]] , book_id:int)->bool:
    return False

def add_book(books:list[dict[str,str|int|bool]] , name:str, author:str,year:int)->bool:
    if not is_non_empty_string(name):
        return False
    if not is_non_empty_string(author):
        return False
    if not is_positive_int(year):
        return False
    if book_in_library(books,name,author)
        return False
    books.append({ "id": get_next_book_id(books),"name": name, "author": author, "year": year,"available": True})
    return True

def add_book_flow(books:list[dict[str,str|int|bool]]):
    name = get_input("Enter the title: ")
    author = get_input("Enter the author: ")
    year = int(get_input("Enter the year: "))
    result = add_book(books,name,author,year)
    if result == True:
        print("Book successfully added!")
    else:
        print("Error invalid value entered!")




    


    