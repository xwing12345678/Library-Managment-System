from books import books
from get_books import get_input, get_book_by_id
from validations import is_non_empty_string, is_positive_int,book_in_library,id_in_library, is_available,is_book_id

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

def borrow_book(books:list[dict[str,str|int|bool]], book_id:int)->bool:
    if not id_in_library(books,book_id):
        return False
    if not is_available(get_book_by_id(books,book_id)): 
        return False
    for book in books:
        if is_book_id(book,book_id):
            book["available"] = False
            return True
    return False
        
def borrow_flow(books:list)->None:
    book_id = get_input("Enter the book_id of the book you want to borrow: ")
    if not is_non_empty_string(book_id):
        print("Empty selection!")
        return None
    if not book_id.isdigit():
        print ("This is not something that can be converted to an integer! ")
        return None
    result = borrow_book(books,int(book_id))
    if result == True:
        print("You have successfully borrowed the book!")
    else:
        print("You did not enter a valid id of an available book.")

def return_book(books:list[dict[str,str|int|bool]] , book_id:int)->bool:    
    if not id_in_library(books,book_id):
            return False
    if is_available(get_book_by_id(books,book_id)): 
            return False
    for book in books:
        if is_book_id(book,book_id):
            book["available"] = True
            return True
    return False

def return_flow(books:list)->None:
    book_id = get_input("Enter the book_id of the book you want to return: ")
    if not is_non_empty_string(book_id):
        print("Empty selection!")
        return None
    if not book_id.isdigit():
        print ("This is not something that can be converted to an integer! ")
        return None
    result = return_book(books,int(book_id))
    if result == True:
        print("You have successfully returned the book!")
    else:
        print("You did not enter a valid id of an borrowed book.")

    
def add_book(books:list[dict[str,str|int|bool]] , name:str, author:str,year:int)->bool:
    if not is_non_empty_string(name):
        return False
    if not is_non_empty_string(author):
        return False
    if not is_positive_int(year):
        return False
    if book_in_library(books,name,author):
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




    


    