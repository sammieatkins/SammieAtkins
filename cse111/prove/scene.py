"""
percentage for arguments (?)
how to make the width and height the actual width and height
"""

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from cgi import print_arguments
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # PROBLEM: !!!!!!!!!!!!!!!!!!!!!!!!
    draw_sky(canvas, scene_width, scene_height + 50)
    draw_ground(canvas, scene_width, 50)

    # draw_grid(canvas, scene_width, scene_height, 50)


    # Call the finish_drawing function in the draw2d.py library.
    finish_drawing(canvas)
# SKY
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, fill="royalBlue4")

    draw_moon_blue(canvas, 250, 375, 200, 200)
    draw_moon_yellow(canvas, 250, 375, 200, 200)
    draw_moon_blue(canvas, 250, 375, 200, 200)

    for x in range(0, scene_width, 30):
        for y in range(50, scene_height, random.randrange(50, 75)):
            draw_stars(canvas, x, random.randrange(2,4), y)

    # small cloud
    draw_cloud(canvas, 150, 300, 150, 150)
    draw_cloud(canvas, 200, 288, 125, 125)
    
    # big cloud
    draw_cloud(canvas, 330, 435, 175, 175)
    draw_cloud(canvas, 380, 422, 150, 150)
    
# GROUND
def draw_ground(canvas, scene_width, height):
    """
    Draws dirt (rectangle), grass blades, and a pine tree.
    Parameters:
        canvas
        scene_width
        height: height you want the ground to be. 
    """
    draw_rectangle(canvas, 0, height, scene_width, 0, fill="saddleBrown", outline="saddleBrown")
    draw_pine_tree(canvas, 600, 50, 350)
    for x in range(0, scene_width, 10):
        draw_grass(canvas, x)
    for x in range(0, scene_width, 20):
        draw_grass(canvas, x, color="green")

# CLOUD
def draw_cloud(canvas, center_x, center_y, width=100, height=100):
    """
    Creates three overlapping circles to form a cloud
    Parameters:
        canvas: duh lol
        center_x: x-value for the center of the top/middle circle
        center_y: y-value for the center of the top/middle circle
        width: width of top/middle circle (optional)
        height: height of top/middle circle (optional)
    """
    # define center_x and center_y based on scene width and scene height 
    # middle circle
    middle_width = width / 1.5
    middle_height = height / 2
    middle_top_x = center_x - middle_width / 2
    middle_top_y = center_y - middle_height / 2
    middle_bottom_x = center_x + middle_width / 2
    middle_bottom_y = center_y + middle_height / 2
    draw_oval(canvas, middle_top_x, middle_top_y, middle_bottom_x, middle_bottom_y, fill="lightSlateGray", outline="lightSlateGray")

    # right circle
    right_center_x = center_x + middle_width / 2
    right_center_y = center_y - middle_height / 2
    right_width = width / 1.5
    right_height = height / 2
    right_top_x = right_center_x - right_width / 2
    right_top_y = right_center_y - right_height / 2
    right_bottom_x = right_center_x + right_width / 2
    right_bottom_y = right_center_y + right_height / 2
    draw_oval(canvas, right_top_x, right_top_y, right_bottom_x, right_bottom_y, fill="lightSlateGray", outline="lightSlateGray")

    # left circle
    left_center_x = center_x - middle_width / 2
    left_center_y = center_y - middle_height / 2
    left_width = width / 1.5
    left_height = height / 2
    left_top_x = left_center_x - left_width / 2
    left_bot_y = left_center_y - left_height / 2
    left_bottom_x = left_center_x + left_width / 2
    left_top_y = left_center_y + left_height / 2
    draw_oval(canvas, left_top_x, left_bot_y, left_bottom_x, left_top_y, fill="lightSlateGray", outline="lightSlateGray")

    # bottom rectangle
    # print(left_center_x)
    # print(center_y)
    # print(right_center_x)
    # print(left_top_y)
    # print(left_bot_y)
    draw_rectangle(canvas, left_center_x, center_y, right_center_x, left_bot_y, fill="lightSlateGray", outline="lightSlateGray")

# MOON
def draw_moon_yellow(canvas, center_x, center_y, width=150, height=150):
    """
    Creates crescent moon by overlapping two circles. The first, a yellow circle, is overlapped by a sky-color circle. 
    Parameters:
        canvas: obvi
        center_x: x-value for yellow moon circle
        center_y: y-value for yellow moon circle
        width: width of yellow moon circle
        height: height of yellow moon circle
    """
    top_x = center_x - width / 2
    top_y = center_y + height / 2
    bot_x = center_x + width / 2
    bot_y = center_y - height / 2
    draw_oval(canvas, top_x, top_y, bot_x, bot_y, fill="gold1", outline="darkGoldenrod")

def draw_moon_blue(canvas, center_x, center_y, width=150, height=150):
    crescent_top_x = center_x - width / 5
    crescent_top_y = center_y + height 
    crescent_bot_x = center_x + width
    crescent_bot_y = center_y - width / 4
    draw_oval(canvas, crescent_top_x, crescent_top_y, crescent_bot_x, crescent_bot_y, fill="royalBlue4", outline="royalBlue4")
 
# GRASS
def draw_grass(canvas, center_x, center_y=50, height=25, width=10, color="darkGreen"):
    top_x = center_x
    top_y = center_y + height
    right_x = center_x + width / 2
    # right_y = center_y 
    left_x = center_x - width / 2
    # left_y = center_y
    draw_polygon(canvas, top_x, top_y, right_x, center_y, left_x, center_y, fill=color, outline=color)

# STARS
def draw_stars(canvas, center_x, height, center_y=300):
    # how to make the size random?
    top_x = center_x - height / 2
    top_y = center_y + height / 2
    bottom_x = center_x + height / 2
    bottom_y = center_y - height / 2
    draw_oval(canvas, top_x, top_y, bottom_x, bottom_y, fill="gold", outline="gold")

# PINE TREE
def draw_pine_tree(canvas, center_x, bottom, height):
    # Draw the tree trunk.
        # pass in lower left and upper right coordinates
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="saddleBrown", outline="saddleBrown")

    # Draw the skirt of the tree
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="darkGreen", outline="darkGreen")

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


    
# draw_pine_tree(canvas, 550, 150, 250)
# draw_pine_tree(canvas, 200, 100, 200)
# for x in range(100, 700, 100):
    #     draw_pine_tree(canvas, x, 250, 80)
 # print(top_x)
    # print(top_y)
    # print(bot_x)    
    # print(bot_y)
    # print()

    # print(crescent_top_x)
    # print(crescent_top_y)
    # print(crescent_bot_x)
    # print(crescent_bot_y)