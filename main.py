from books import books
import validations as v
valid_menu_choices = [str(integer) for integer in range(1,9)]
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
            print("Not implemented yet! Chose another option!")

        elif choice == '1':
            print("Not implemented yet! Chose another option!")

        elif choice == '2':
                    print("Not implemented yet! Chose another option!")
        
        elif choice == '3':
            print("Not implemented yet! Chose another option!")
        elif choice == '4':
                    print("Not implemented yet! Chose another option!")
        elif choice == '5':
                    print("Not implemented yet! Chose another option!")
        elif choice == '6':
                    print("Not implemented yet! Chose another option!")
        elif choice == '7':
                    print("Not implemented yet! Chose another option!")
        else:
            print("Thanks for using the library management system!",
                  "Hope to see you again soon!")
            not_exited = False
            break 
main()
