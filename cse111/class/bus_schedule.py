from datetime import datetime 

# Ask for information: stop/street, bus #, how full
street = input("What is the street for your stop? ")
bus_number = input("What is the bus number? ")
    # better to leave this as a string because it could be 17E or something. plus not using as a number
capacity = float(input("How full is the bus (%)? "))

# Clean up variables
street = street.strip().title()
    # how to get the Th to be fixed?
bus_number = bus_number.strip().upper()
    # you can chain the methods because these are strings. reads left to right. order doesn't really matter (?)

# Convert decimal percents to whole numbers
if capacity > 0 and capacity < 1:
    capacity *= 100

# Find the current day and time
today = datetime.now()
    # formatting options link in cse 111 prove instructions

# Add to a text file
    # notes "for with open()"    
        # NO UNDO BUTTON HERE AHHHHHHHHHHHH
        # this will create a file, if it already exists it will override 
        # you have to run the program for the file to be created
        # optional parameters: ("filename", *default is reading* *t is for TEXT* "rt", *w is for WRITING* "wt", *a is for APPEND* "at")
            # use append for prove assignment
with open("bus_data.csv", "at") as bus_file:
   print(f"{today:%Y-%m-%d},{street},{bus_number},{capacity:.0f}%", file=bus_file)
    # Named parameters do not use spaces between variables

# Display a message to the user saying it has been recorded 
print(f"{today},{street},{bus_number},{capacity:.0f}% has been recorded. :)")