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

    choice = -1

    while choice != 4:
        # Print menu.
        print_main_menu()
        try:
            # Get user choice from menu.
            print()
            choice = int(input("Enter a menu item (ex: 1): "))
            if choice == 1:
                # books_dict = add_book(rows)
                add_book(rows, books_dict)
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
            else:
                print("Please enter a number between 1 and 4")

        except ValueError:
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
        books_dict = dictionary to sort [Key: Title, Author, Time Entered]
        sort_by = duh
    """
    if sort_by == 1:
        ### sort by date entered  
        books_list = sorted(books_dict.items(), key=lambda x:x[1][0])
        sortdict = dict(books_list)
        for item in sortdict:
            print(f"{sortdict[item][2]}, {sortdict[item][0]}, {sortdict[item][1]}")
    elif sort_by == 2:
        ### sort by author
        books_list = sorted(books_dict.items(), key=lambda x:x[1][1])
        sortdict = dict(books_list)
        for item in sortdict:
            print(f"{sortdict[item][1]}, {sortdict[item][0]}, {sortdict[item][2]}")
    elif sort_by == 3:
        # Sort by title.
        books_list = sorted(books_dict.items(), key=lambda books_dict: books_dict[1][0][4:] if books_dict[1][0][:3].lower() == "the" else books_dict[1][0])
        sortdict = dict(books_list)
        for item in sortdict:
            print(f"{sortdict[item][0]}, {sortdict[item][1]}, {sortdict[item][2]}")
    elif sort_by == 4:
        return

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
        # print(f"{key}. {title}, {author}, {date}")
        
        count = 0
        for _ in dictionary:
            count += 1
            print(f"{count}. {title}, {author}, {date}")
        print()

def add_book(rows, books_dict):
    """
    Asks user for title and author of the book they read and enters it into "books.csv"
    Parameters:
        books_dict
    Returns:
        new_dict
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
                print(f"{rows},{title},{author.title()},{date: %Y-%m-%d %I:%M:%S}", file=books_file)
                ##################
                # new_key = books_dict.keys[KEY_COLUMN_INDEX] + 1
            # books_dict[new_key] = title, author, date
        elif confirm == "n":
            print("Oops!! Let's try again :)")
    print(f"{title}, {author.title()}, {date: %Y-%m-%d %I:%M:%S} has been added to the list :)")
    # new_dict = read_dict("books.csv", KEY_COLUMN_INDEX)
    # return new_dict

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
        ## try block here
            ## within length of the list
            ## number
            ## above 0
    ######### figure out better situation with try blocks?

    good_input = False

    while good_input == False:
        try:
            remove_key = input("Which book do you want to remove (ex: 1)? ")
        except ValueError:
            good_input = False
            print("Please enter a number.")
        if remove_key < 0:
            good_input = False
            print("That number is not in the list. Please try again.")
        elif len(remove_key) != 1:
            good_input = False
            print("Too many characters. Please try again.")
        elif remove_key > len(books_dict):
            good_input = False
            print("That number is not in the list. Please try again.")
        else:
            good_input = True
            # Remove that item from the list.
            del books_dict[remove_key]
            print_dict(books_dict)

    # # Fix key values so they are in order again
    # fixed_dict = fix_keys(books_dict)
    
    # # Delete old file
    # delete_file("books.csv")
    
    # # Make new file from fixed dictionary
    # make_new_file("books.csv", fixed_dict)

# def fix_keys(new_dict):
#     """
    
#     """
#     count = 0
#     fixed_dict = {}
#     for value in new_dict.values():
#         count += 1
#         fixed_dict[count] = value
#     return fixed_dict

# def delete_file(filename):
#     os.remove(filename)

# def make_new_file(filename, fixed_dict):
#     with open(filename) as books_file:
#         print("Key, Title, Author, Time Entered")
#         for key, values in fixed_dict.items():
#             print(f"{key}, {values}")

if __name__ == "__main__":
    main()