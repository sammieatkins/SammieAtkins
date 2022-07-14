# how many # signs and what they mean
    ################ = question / important note
    # = Note to stay in program.
    # = commented out code
    ## = heading of note to stay in program
    ### = personal note

# Imports.
from datetime import datetime
import csv
import os
import operator
# import requests
# import random

########## CAREFUL DON'T RUN YET BC NOT SURE IF DELETE THING WORKS RIGHT ##########

##########
# sort function - don't know what's going on
# try block/while loop situation in main
    # turn into a function?
# add genre and sort by that? is there a way to make that optional?

# Constants.
KEY_COLUMN_INDEX = 0

def main():
    books_dict, rows = read_dict("books.csv", KEY_COLUMN_INDEX)

    # Print menu.
    print_main_menu()

    # choice = -1

    ########### try block or while loop? ############
    # while choice >= 1 and choice <= 4:
    try:
        # Get user choice from menu.
            ### try block here
        print()
        choice = int(input("Enter a menu item (ex: 1): "))
        if choice == 1:
            add_book(rows)
        elif choice == 2:
            remove_book(books_dict)
        elif choice == 3:
            ### try block here to make sure they input the right number
            display_choice = print_display_menu()
            ### can sort be it's own function and parameter is menu option/sorting by thing?
            sort_books(books_dict, display_choice)      
        elif choice == 4:
            ### change message?
            print("See you later!! :)")

    except ValueError:
        if choice < 1:
            print("Please enter a number between 1 and 4")
        elif choice > 4:
            print("Please enter a number between 1 and 4")

def print_main_menu():
    """
    Prints menu for user
    Parameters:
        none
    Returns:
        none
    """
    ### add "hello welcome to *insert name of program here*" message?
    print()
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Display book list")
    print("4. Quit")
    print()

def print_display_menu():
    # title and author alphabetical
    print()
    print("Display by...")
    print("1. Date entered")
    print("2. Author")
    print("3. Title")
    print("4. Return to main menu")
    print()
    display_choice = int(input("Enter a display option (ex: 1): "))
    return display_choice

def sort_books(books_dict, sort_by):
    """
    User sees:
    Display by...
        1. Date entered
        2. Author
        3. Title
        4. Return to main menu
    Sorts books_dict by given parameter. 
    Parameters:
        books_dict = dictionary to sort
        sort_by = duh
    """
    if sort_by == 1:
        ### sort by date entered
        books_list = sorted(books_dict.items(), key=lambda x:x[1])
        sortdict = dict(books_list)
        print_dict(sortdict)
    elif sort_by == 2:
        ### sort by author
        books_list = sorted(books_dict.items(), key=lambda x:x[1])
        sortdict = dict(books_list)
        print_dict(sortdict)
    elif sort_by == 3:
        ### sort by title
        pass

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: 
        books_dict: a compound dictionary that contains
        the contents of the CSV file.
        rows
    """
    books_dict = {}
    rows = 0
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for row_list in reader:
            rows += 1
            if len(row_list) != 0:
                key = row_list[key_column_index]
                ### 1: assumes to the end
                books_dict[key] = row_list[1:]
    return books_dict, rows + 1

def print_dict(dictionary):
    for key, value in dictionary.items():
        title = value[0]
        author = value[1]
        date = value[2]
        print(f"{key}. {title}, {author}, {date}")
        print()

def add_book(rows):
    """
    Asks user for title and author of the book they read and enters it into "books.csv"
    Parameters:
        books_dict
    Returns:
        none
    """
    confirm = "n"
    while confirm == "n":
        print()
        title = input("Enter the book title: ")
        author = input("Enter the author of the book: ")
        print()

        confirm = input(f"Are you sure you want to add {title} by {author} y/n? ")
        if confirm == "y":
            date = datetime.now()
            with open("books.csv", "at") as books_file:
                print(f"{rows}, {title}, {author.title()}, {date: %Y-%m-%d %I:%M:%S}", file=books_file)
        elif confirm == "n":
            print("Oops!! Let's try again :)")
    print(f"{title}, {author.title()}, {date: %Y-%m-%d %I:%M:%S} has been added to the list :)")

def remove_book(books_dict):
    """
    Removes book from list and fixes keys to be in order again. 
    Parameter:
        books_dict: dictionary to remove something from
    Returns:
        fixed_dict
    """
    # Print dictionary for user to see.
    print_dict(books_dict)

    # Ask for number they want to remove.
        ### try block here
            ### within length of the list
            ### number
            ### above 0
    remove_key = input("Which book do you want to remove (ex: 1)? ")
    
    # Remove that item from the list.
    del books_dict[remove_key]

    # Fix key values so they are in order again
    fixed_dict = fix_keys(books_dict)
    
    # Delete old file
    delete_file("books.csv")
    
    # Make new file from fixed dictionary
    make_new_file("books.csv", fixed_dict)

def fix_keys(new_dict):
    """
    
    """
    count = 0
    fixed_dict = {}
    for value in new_dict.values():
        count += 1
        fixed_dict[count] = value
    return fixed_dict

def delete_file(filename):
    os.remove(filename)

def make_new_file(filename, fixed_dict):
    with open(filename) as books_file:
        print("Key, Title, Author, Time Entered")
        for key, values in fixed_dict.items():
            print(f"{key}, {values}")

if __name__ == "__main__":
    main()