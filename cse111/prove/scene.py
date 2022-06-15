# Import the functions from the Draw 2-D library
# so that they can be used in this program.
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
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, fill="lightSkyBlue")
    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_pine_tree(canvas, 550, 150, 250)
    draw_pine_tree(canvas, 200, 100, 200)

    for x in range(100, 700, 100):
        draw_pine_tree(canvas, x, 250, 80)

    draw_grid(canvas, scene_width, scene_height, 50)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_pine_tree(canvas, center_x, bottom, height):
    # Draw the tree trunk.
        # pass in lower left and upper right coordinates
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="tan4")

    # Draw the skirt of the tree
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="forestGreen")

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