from validations import is_non_empty_string

def display_books(books:list[dict[str,str|int|bool]])->None:
    for book in books:
        print(book)



def search_book(books:list[dict[str,str|int|bool]], name:str)->dict[str,str|int|bool]|list[dict[str,str|int|bool]]|None:
    pass