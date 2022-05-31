# Imports.
from cmath import pi
import math

# Functions. 
def compute_area_square(side):
    return side * side

def compute_area_rectangle(length,width):
    return length * width

def compute_area_circle(radius):
    return 2 * math.pi * radius 

# Variables.
shape = ""

# Loop. 
while shape != "":
    shape = input("What shape would you like to input? ")
    shape = shape.lower()

    # Square.
    if shape == "square":
        square = float(input("What is the side of the square? "))
        square_area = compute_area_square(square)
        print(f"The area is {square_area}")
    
    # Square.
    elif shape == "rectangle":
        rectangle_length = float(input("What is the length of the rectangle? "))
        rectangle_width = float(input("What is the width of the rectangle? "))
        rectangle_area = compute_area_rectangle(rectangle_length,rectangle_width)
        print(f"The area is {rectangle_area}")

    # Circle.
    elif shape == "circle":
        circle = float(input("What is the radius of the circle? "))
        circle_area = compute_area_circle(circle)
        print(f"The area is {circle_area}")

    # Try again.
    else:
        print("Not an option, please try again. ")