import math

# inputs
number_of_items = int(input("Enter number of items: "))
items_per_box = int(input("Enter number of items per box: "))

# compute number of boxes
number_of_boxes = number_of_items / items_per_box
rounded_boxes = math.ceil(number_of_boxes)

# display
print(f"For {number_of_items} items, packing {items_per_box} items in each box, you will need {rounded_boxes} boxes.")