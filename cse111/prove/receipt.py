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
Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
"""

def main():
    try:
        # create dictionary
        products_dict = read_dict("products.csv", ITEM_ID_INDEX)
        with open("request.csv", "rt") as file:
            reader = csv.reader(file)
            next(reader)
            requests = []
            for line in reader:
                requests.append(line)
            # print(requests)

            # Print the store name at the top of the receipt.
            print()
            print("Inkom Emporium")
            print()

            # Print the list of ordered items.
            get_requested_items(products_dict, requests)
            print()
            
            # Sum and print the number of ordered items.
            count = count_items(requests)
            print(f"Number of items: {count}")

            # Check for discount
            tuesday = check_discount()

            # Sum and print the subtotal due.
            subtotal = calculate_subtotal(products_dict, requests, tuesday)
            print(f"Subtotal: ${subtotal:.2f}")

            # Compute and print the sales tax amount.
            sales_tax = calculate_sales_tax(subtotal)
            print(f"Sales tax: ${sales_tax:.2f}")

            # Compute and print the total amount due.
            total = calculate_total(subtotal, sales_tax)
            print(f"Total: ${total:.2f}")

            # Print a thank you message.
            print()
            print("Thank you for shopping at the Inkom Emporium.")

            # Get the current date and time from your computer's operating system and print the current date and time.
            print_date()
            print()
    except FileNotFoundError as msg:
        print()
        print("Error: missing file")
        print(msg)
        print()
    except PermissionError:
        print()
        print("Sorry, it seems you do not have permission to open this file.")
        print()
    except KeyError as key:
        print()
        print(f"Error: unknown product ID in the request.csv file '{key}'")
        print()

def check_discount():
    """
    Checks if the day is Tuesday. 
    Parameters:
        none
    Returns:
        tuesday: If it is Tuesday, the tuesday variable will be returned as True (boolean variable). If not, tuesday is False.
    """
    tuesday = False

    day = datetime.now()
    # Monday = 0, Tuesday = 1, etc.
    day = day.weekday()
    print(day)

    if day == 1:
        tuesday = True

    return tuesday

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
    item = products_dict[product_number][index]
    return item

def get_requested_items(products_dict, requests):
    """
    Reads "request.csv" file. Prints product name, quantity, and price.
    Parameter:
        products_dict 
    Returns:
        none
    """

    print("Requested items:")
    for line in requests:
        product_number = line[ITEM_ID_INDEX]
        product_name = find_index(products_dict, product_number, ITEM_NAME_INDEX)
        quantity = line[1]
        price = find_index(products_dict, product_number, ITEM_PRICE_INDEX)
        print(f"{product_name}: {quantity} @ {price}")

def count_items(requests):
    """
    Counts number of lines in csv file and prints it out.
    Parameter:
        requests: list of requests
    Returns:
        quantity: the number of items in the list
    """
    quantity = 0

    for line in requests:
        quantity += int(line[ITEM_QUANTITY_INDEX])
    return quantity

def calculate_subtotal(products_dict, requests, tuesday):
    """
    Sums the subtotal due.
    Parameter:
        requests: list of requests
    Returns:
        price: subtotal
    """
    price = 0
    for line in requests:
        product_number = line[ITEM_ID_INDEX]
        quantity = float(line[ITEM_QUANTITY_INDEX])
        price_index = float(find_index(products_dict, product_number, ITEM_PRICE_INDEX))
        price += price_index * quantity
        if tuesday == True:
            amount = price * .10
            price -= amount
    return price

def calculate_sales_tax(subtotal):
    """
    Computes and prints the sales tax amount. Uses 6% as the sales tax rate.
    Parameters:
        subtotal
    Returns:
        sales_tax
    """
    return subtotal * .06

def calculate_total(subtotal, sales_tax):
    """
    Computes the total amount due.
    Parameters:
        subtotal
        sales_tax
    Returns:
        total
    """
    return subtotal + sales_tax

def print_date():
    # Call the now() method to get the current date and time as a datetime object from the computer's operating system.
    current_date_and_time = datetime.now()

    # Print the current day of the week and the current time.
    print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")

if __name__ == "__main__":
    main()