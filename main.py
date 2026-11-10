from books import books
import validations as v
from get_books import display_books, book_name_flow,get_available_books, books_by_author_flow
from set_books import add_book_flow, borrow_flow
valid_menu_choices:list[str] = [str(integer) for integer in range(1,9)]

main_menu_message = '''
================================
       LIBRARY MANAGEMENT
================================

1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author
8. Exit

Choose an option:   '''

def main():
    not_exited:bool = True
    while not_exited == True:
        choice = v.get_valid_menu_choice(main_menu_message,valid_menu_choices)
        if choice == '1':
            display_books(books)        
        elif choice == '2':
                book_name_flow(books)
        elif choice == '3':
              add_book_flow(books)

        elif choice == '4':
            borrow_flow(books)
        
        elif choice == '5':
                    print("Not implemented yet! Chose another option!")

        elif choice == '6':
            print(get_available_books(books))
        elif choice == '7':
            books_by_author_flow(books)              
        # must have chosen 8 so we exit
        else:
            print("Thanks for using the library management system!",
                  "Hope to see you again soon!")
            not_exited = False
            break 
main()
