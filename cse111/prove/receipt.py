import csv

# products.csv
ITEM_ID_INDEX = 0
ITEM_NAME_INDEX = 1
ITEM_PRICE_INDEX = 2

# request.csv
ITEM_ID_INDEX = 0
ITEM_QUANTITY_INDEX = 1

def main():
    """
    Contains a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
        Use the requested product number to find the corresponding item in the products_dict.
        Print the product name, requested quantity, and product price.
    """

    products_dict = read_dict("products.csv", ITEM_ID_INDEX)
    print(products_dict)
    with open("request.csv", "rt") as file:
        reader = csv.reader(file)
        next(reader)
        print("Requested items:")
        for line in reader:
            product_number = line[ITEM_ID_INDEX]
            product_name = find_name(products_dict, product_number)
            quantity = line[1]
            price = find_price(products_dict, product_number)
            print(f"{product_name}: {quantity} @ {price}")

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

def find_name(products_dict, product_number):
    # index parameter - combine functions
    """
    Finds name of item in provided dictionary based on the product number.
    """
    if product_number in products_dict:
        # gets name
        name = products_dict[product_number][ITEM_NAME_INDEX]
    else:
        name = "No such name"
    return name

# def find_quantity(file):
#     """
    
#     """
#     quantity = line[1]
    

    
    # if product_number in file:
    #     quantity = file[ITEM_QUANTITY_INDEX]
    # else:
    #     quantity = "No such quantity"
    # return quantity 

def find_price(products_dict, product_number):
    """
    Finds price of item in provided dictionary based on the product number.
    """
    if product_number in products_dict:
        price = products_dict[product_number][ITEM_PRICE_INDEX]
    else:
        price = "No such price"
    return price



if __name__ == "__main__":
    main()