# imports
import math
from datetime import datetime

# inputs
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# calculations
    # WHaat is going on here - DONT USE COMMAS TO SEPARATE BIG NUMBERS
volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# current date
today = datetime.now()

# display
print(f"The approximate volume is {volume:.2f} liters. ")

# phone number
ask_buy = input("Would you like to buy tires with these dimensions (yes/no)? ")

if ask_buy.lower() == "yes":
    phone_number = input("Please enter your phone number (123-456-7890: ")

# add to volumes.txt
with open("volumes.txt", "at") as volumes_file:
    if ask_buy.lower() == "yes":
        print(f"{today:%Y-%m-%d},{width},{aspect_ratio},{diameter},{volume:.2f},{phone_number}", file=volumes_file)
    else:
        print(f"{today:%Y-%m-%d},{width},{aspect_ratio},{diameter},{volume:.2f}", file=volumes_file)
