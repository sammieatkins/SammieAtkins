# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from cgi import print_arguments
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    # draw_pine_tree(canvas, 550, 150, 250)
    # draw_pine_tree(canvas, 200, 100, 200)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, 150)

    # for x in range(100, 700, 100):
    #     draw_pine_tree(canvas, x, 250, 80)

    draw_grid(canvas, scene_width, scene_height, 50)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, fill="skyBlue1")
    #cloud 1
    draw_cloud(canvas, 150, 400)
    draw_cloud(canvas, 250, 450, 200, 200)
    draw_cloud(canvas, 450, 350)

def draw_ground(canvas, scene_width, height):
    draw_rectangle(canvas, 0, height, scene_width, 0, fill="tan4")

# def draw_clouds 
    # make this overlap many circles to make an actual cloud :)

# def draw_cloud(canvas, center_x, bottom, width, height):
#     top_x = center_x - width / 2
#     top_y = bottom + height
#     bottom_x = center_x + width / 2
#     # bottom_y is bottom

#     draw_oval(canvas, top_x, top_y, bottom_x, bottom, fill="white")

def draw_cloud(canvas, center_x, center_y, width=100, height=100):
    # middle circle
    middle_width = width / 1.5
    middle_height = height / 2
    middle_top_x = center_x - middle_width / 2
    middle_top_y = center_y - middle_height / 2
    middle_bottom_x = center_x + middle_width / 2
    middle_bottom_y = center_y + middle_height / 2
    draw_oval(canvas, middle_top_x, middle_top_y, middle_bottom_x, middle_bottom_y, fill="white", outline="black")

    # right circle
    right_center_x = center_x + middle_width / 2
    right_center_y = center_y - middle_height / 2
    right_width = width / 1.5
    right_height = height / 2
    right_top_x = right_center_x - right_width / 2
    right_top_y = right_center_y - right_height / 2
    right_bottom_x = right_center_x + right_width / 2
    right_bottom_y = right_center_y + right_height / 2
    draw_oval(canvas, right_top_x, right_top_y, right_bottom_x, right_bottom_y, fill="white", outline="white")

    # left circle
    left_center_x = center_x - middle_width / 2
    left_center_y = center_y - middle_height / 2
    left_width = width / 1.5
    left_height = height / 2
    left_top_x = left_center_x - left_width / 2
    left_bot_y = left_center_y - left_height / 2
    left_bottom_x = left_center_x + left_width / 2
    left_top_y = left_center_y + left_height / 2
    draw_oval(canvas, left_top_x, left_bot_y, left_bottom_x, left_top_y, fill="white", outline="white")

    # bottom rectangle
    print(left_center_x)
    print(center_y)
    print(right_center_x)
    print(left_top_y)
    print(left_bot_y)
    draw_rectangle(canvas, left_center_x, center_y, right_center_x, left_bot_y, fill="white", outline="white")


   



# def draw_pine_tree(canvas, center_x, bottom, height):
#     # Draw the tree trunk.
#         # pass in lower left and upper right coordinates
#     trunk_width = height / 10
#     trunk_height = height / 8
#     left_trunk = center_x - trunk_width / 2
#     bottom_trunk = bottom
#     right_trunk = center_x + trunk_width / 2
#     trunk_top = bottom + trunk_height
#     draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="tan4")

#     # Draw the skirt of the tree
#     skirt_width = height / 2
#     skirt_left = center_x - skirt_width / 2
#     skirt_bottom = trunk_top
#     peak_x = center_x
#     peak_y = bottom + height
#     skirt_right = center_x + skirt_width / 2
    
#     draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="forestGreen")

def draw_grid(canvas, width, height, interval):
    # Draw vertical line. 
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")
    
    # Draw horizontal line. 
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")


# Call the main function so that
# this program will start executing.
main()