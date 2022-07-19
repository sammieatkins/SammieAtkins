# Imports.
from datetime import datetime
import csv

# Constants.
BOOK_NUMBER_INDEX = 0
TITLE_INDEX = 1
AUTHOR_INDEX = 2
DATE_ENTERED_INDEX = 3

###### write doc strings!!
###### how to update the books list after they add a book? - they should be able to print it and have an updated number of books read
###### remove doesn't work :(
###### test_count_books_read()

def main():   
    get_choice()
    
    new_books_list = make_list("books.csv")

    books_read = count_books_read(new_books_list)
    print(f"You've read {books_read} books!!")

def make_list(filename):
    """
    Creates a list from a csv file. 
    Parameter:
        filename
    Returns:
        list: the list of the things in each row
        rows: the number of rows in the file, skipping the header row
    """
    list = []
    rows = 0
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            rows += 1
            list.append(line)
    return list, rows + 1

def print_main_menu():
    """
    Prints menu for user
    Parameters:
        none
    Returns:
        none
    """
    print()
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Display book list")
    print("4. Quit")

def print_display_menu():
    print()
    print("Display by...")
    print("1. Title")
    print("2. Author")
    print("3. Date Entered")
    print("4. Return to main menu")
    print()

def print_list(list, sort_by):
    for line in list:
        number = line[BOOK_NUMBER_INDEX]
        title = line[TITLE_INDEX]
        author = line[AUTHOR_INDEX]
        date = line[DATE_ENTERED_INDEX]

        # Normal print.
        if sort_by == 0:
            print()
            print(f"{number}. {title}, {author}, {date}")
        
        # Print by title.
        elif sort_by == 1:
            print(f"{title}, {author}, {date}")

        # Print by date.
        elif sort_by == 3:
            print(f"{date}, {title}, {author}")
        
        # Print by author.
        elif sort_by == 2:
            print(f"{author}, {title}, {date}")

def get_choice():
    choice = -1

    while choice != 4:
        # Read file.
        books_list, rows = make_list("books.csv")

        # Print menu.
        print_main_menu()
        try:
            # Get user choice from menu.
            print()
            choice = int(input("Enter a menu item: "))
            # Add a book to the list.
            if choice == 1:
                add_book(books_list, rows)
            # Remove a book from the list.
            elif choice == 2:
                remove_book(books_list)
            # Display the books list.
            elif choice == 3:
                # Get user input from menu and sort by display choice.
                sort_books(books_list)      
            # End program
            elif choice == 4:
                break
            else:
                raise ValueError
        except ValueError as val_err:
            print(f"Please enter a number between 1 and 4. {val_err}")

def add_book(books_list, rows):
    """
    returns:
        none
    """
    confirm = "n"
    while confirm == "n":
        print()
        title = input("Enter the book title: ")
        author = input("Enter the author of the book: ")
        print()

        confirm = input(f"Are you sure you want to add {title} by {author} (y/n)? ")
        if confirm == "y":
            date = datetime.now()
            with open("books.csv", "at") as books_file:
                print(f"{rows},{title},{author.title()},{date:%Y-%m-%d %I:%M:%S}", file=books_file)
        elif confirm == "n":
            print("Oops!! Let's try again :)")
    print(f"{title}, {author.title()}, {date:%Y-%m-%d %I:%M:%S} has been added to the list :)")

def remove_book(books_list):
    ####### how to handle if they enter in multiple numbers?
    ####### fix try blocks?

    # elif len(remove_key) != 1:
    #     good_input = False
    #     print("Too many characters. Please try again.")

    # Print list for user to see.
    print_list(books_list, 0)

    good_input = False
    # books_dict_length = len(books_dict)
    while good_input == False:
        try:
            print("Enter -1 to return to main menu.")
            
            # Ask for number they want to remove.
            remove_index = int(input("Which book do you want to remove? "))

            # Check if number is negative (ignoring the -1 to return to main menu). 
            if remove_index < -1:
                raise ValueError

            # Check if number is greater than the length of the books list. 
            elif remove_index > len(books_list):
                raise ValueError

            # Return to main menu if they enter -1.
            elif remove_index == -1:
                break
            
            # If key is valid, remove that index from the list.
            ###### should I remove it from the file and then re-read it into a new list?
            else:
                books_list.pop(remove_index - 1)
                
                # Open file for writing.
                with open("books.csv", "w") as books_file:
                    print("Book Number, Title, Author, Date Entered", file=books_file)
                    line_number = 0
                    for line in books_list:
                        line_number += 1
                        title = line[TITLE_INDEX]
                        author = line[AUTHOR_INDEX]
                        date = line[DATE_ENTERED_INDEX]
                        print(f"{line_number},{title},{author.title()},{date}", file=books_file)
                # print_list(books_list, 0)
                good_input = True

        ###### How to handle letters separately?
        # except TypeError as type_err:
        #     print(f"Please enter a number. {type_err}")
        #     print()
        except ValueError as val_err:
            print(f"That number is not in the list. Please try again. {val_err}")
            print()

def find_author(book):
    """
    Finds author's last name.
    Parameters:
        books_list: list of books in format "Book Number, Title, Author, Date Entered"
    Returns:
        last_name: author's last name
    """
    last_name = "error"
    author = book[2]
    author = author.split()
    last_name = author[-1]
    last_name = last_name.upper()
    return last_name  
   
def sort_books(books_list):
    """
    User sees:
    Display by...
        1. Title
        2. Author
        3. Date entered
        4. Return to main menu
    Parameters:   
    """
    display_choice = 0
    while display_choice != 4:
        # Print display menu
        print_display_menu()

        # Get display choice.
        display_choice = int(input("Enter a display option: "))

        # Sort by title.
        if display_choice == 1:
            sorted_list = sorted(books_list, key=lambda books_list:books_list[TITLE_INDEX][4:].upper() if books_list[TITLE_INDEX][:3] == "The" else books_list[TITLE_INDEX].upper())
            print_list(sorted_list, display_choice)

        # Sort by author.
        elif display_choice == 2:
            # last_name = find_author(books_list)
            sorted_list = sorted(books_list, key=find_author)
            print_list(sorted_list, display_choice)

        # Sort by date entered.
        elif display_choice == 3:
            sorted_list = sorted(books_list, key=lambda books_list:books_list[DATE_ENTERED_INDEX])
            print_list(sorted_list, display_choice)

        # Return to main menu.
        elif display_choice == 4:
            return

def count_category(books_list, category):
    """
    Counts number of books under certain category given by user (ex: author) are in the list.
    Ex: user types in author, then the author they want to search for. Function returns the number of 
    """
    if category.lower == "author":
        search_author = input("Enter the author to search for: ")
    pass

###### returning 2 books?
def count_books_read(books_list):
    """
    Calculates number of books read.
    Parameter:
        books_list: list of books
    Return:
        books_read: number of books read
    """
    books_read = 0
    for _ in books_list:
        books_read += 1
    return books_read



if __name__ == "__main__":
    main()