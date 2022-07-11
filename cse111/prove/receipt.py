import csv
from datetime import datetime

# products.csv
ITEM_ID_INDEX = 0
ITEM_NAME_INDEX = 1
ITEM_PRICE_INDEX = 2

# request.csv
ITEM_ID_INDEX = 0
ITEM_QUANTITY_INDEX = 1

"""
Print the store name at the top of the receipt.
Print the list of ordered items.
Sum and print the number of ordered items.
Sum and print the subtotal due.
Compute and print the sales tax amount. Use 6% as the sales tax rate.
Compute and print the total amount due.
Print a thank you message.
Get the current date and time from your computer's operating system and print the current date and time.
Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
"""

def main():
    """
    Contains a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
        Use the requested product number to find the corresponding item in the products_dict.
        Print the product name, requested quantity, and product price.
    """
    products_dict = read_dict("products.csv", ITEM_ID_INDEX)
    # print(products_dict)

    with open("request.csv", "rt") as file:
        reader = csv.reader(file)
        next(reader)

        # Print the store name at the top of the receipt.
        print()
        print("Inkom Emporium")
        print()

        # Print the list of ordered items.
        get_requested_items(products_dict, reader)
        print()
        
        # Sum and print the number of ordered items.
        count_items(reader)
        print()
        
        # Sum and print the subtotal due.
        calculate_subtotal(products_dict, reader)

        # Compute and print the sales tax amount.
        calculate_sales_tax()

        # Compute and print the total amount due.
        calculate_total()

        # Print a thank you message.
        print("Thank you for shopping at the Inkom Emporium.")

        # Get the current date and time from your computer's operating system and print the current date and time.
        print_date()


# make things print out in function
def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                products_dict[key] = row_list
    return products_dict

def find_index(products_dict, product_number, index):
    """
    Finds name of item in provided dictionary based on the product number.
    Parameters:
        products_dict: dictionary
        product_number: product number to search for
        indexd: index you want to search for
    Returns: the index searched for. If not found will return "!"
    """
    if product_number in products_dict:
        item = products_dict[product_number][index]
    else:
        item = "!"
    return item

def get_requested_items(products_dict, reader):
    """
    Reads "request.csv" file. Prints product name, quantity, and price.
    Parameter:
        products_dict 
    Returns:
        none
    """

    print("Requested items:")
    for line in reader:
        product_number = line[ITEM_ID_INDEX]
        product_name = find_index(products_dict, product_number, ITEM_NAME_INDEX)
        quantity = line[1]
        price = find_index(products_dict, product_number, ITEM_PRICE_INDEX)
        print(f"{product_name}: {quantity} @ {price}")

def count_items(reader):
    """
    Counts number of lines in csv file and prints it out.
    Parameter:
        reader: list already read as csv file and skipped header row.
    Returns:
        none
    """
    count = 0
    for _ in reader:
        count += 1
    print(f"Number of items: {count}")

def calculate_subtotal(products_dict, reader):
    """
    Computes and prints the sales tax amount. Uses 6% as the sales tax rate.
    Parameters:
        products_dict: 
        reader: list already read as csv file and skipped header row.
    Returns:
        none
    """
    price = 0
    for line in reader:
        product_number = line[ITEM_ID_INDEX]
        price += float(find_index(products_dict, product_number, ITEM_PRICE_INDEX))
    print(f"Subtotal: ${price}")

def calculate_sales_tax():
    pass

def calculate_total():
    pass
def print_date():
    # Call the now() method to get the current date and time as a datetime object from the computer's operating system.
    current_date_and_time = datetime.now()

    # Print the current day of the week and the current time.
    print(f"{current_date_and_time:%A %I:%M %p}")
if __name__ == "__main__":
    main()