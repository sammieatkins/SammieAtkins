# Imports.
from datetime import datetime
import csv

# Constants.
BOOK_NUMBER_INDEX = 0
TITLE_INDEX = 1
AUTHOR_INDEX = 2
DATE_ENTERED_INDEX = 3

###### write doc strings!!

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
    """
    Prints menu for user
    Parameters:
        none
    Returns:
        none
    """
    print()
    print("Display by...")
    print("1. Title")
    print("2. Author")
    print("3. Date Entered")
    print("4. Return to main menu")
    print()

def print_list(books_list, sort_by):
    """
    Prints list of books based on what they are sorted by. Different format for title, author, date, and a normal print out.
    Parameters:
        books_list: list to print out
        sort_by: 
            0 = normal print
            1 = prints: title, author, date
            2 = prints: author, title, date
            3 = prints: date, title, author
    Returns:
        none
    """
    for line in books_list:
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

        # Print by author.
        elif sort_by == 2:
            print(f"{author}, {title}, {date}")

        # Print by date.
        elif sort_by == 3:
            print(f"{date}, {title}, {author}")

def get_choice():
    """
    Gets user choice based on the menu and loops through until they enter 4 to quit. 
    User sees:
        1. Add a book
        2. Remove a book
        3. Display book list
        4. Quit
    Parameters:
        none
    Returns:
        none
    """
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
                add_book(rows)
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

def add_book(rows):
    """
    Adds a book to the compound list of books in the form of a list including [row #,title,author,date entered]
    Parameter:
        rows: comes from make_list() function. essentially the length of the list.
    Returns:
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
    """
    Displays the list for the user to see. User enters the number associated with the book and function removes that from the list and 
    re-reads the dictionary.
    Parameter:
        books_list
    Returns:
        none
    """
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
    Prints out sorted book list based on what the user chooses from the display menu. 
    User sees:
    Display by...
        1. Title
        2. Author
        3. Date entered
        4. Return to main menu
    Parameters:   
        books_list
    Returns:
        none
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

def count_books_read(books_list):
    """
    Calculates number of books read.
    Parameter:
        books_list: list of books
    Return:
        books_read: number of books read
    """
    books_read = 0
    for _ in books_list[0]:
        books_read += 1
    return books_read 

if __name__ == "__main__":
    main()