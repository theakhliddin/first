"""
    Draws a flag with a flagpole, a rectangular flag, and a circle on the flag.
    Parameters:
    x (int): The x-coordinate of the bottom-left corner of the flagpole.
    y (int): The y-coordinate of the bottom-left corner of the flagpole.
    scale_factor (float): The factor by which to scale the dimensions of the flag and flagpole.
    The function performs the following steps:
    1. Draws the flagpole at the specified coordinates with the given height.
    2. Draws a rectangle representing the flag at the top of the flagpole.
    3. Draws a circle on the flag.
    Note: The functions `draw_flagpole`, `draw_rectangle`, and `draw_circle` are assumed to be defined elsewhere.
    """
# Draw a flag with a flagpole, a rectangular flag, and a circle on the flag.
import turtle as t

def draw_side(width, height):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
# Draw a rectangle with the specified dimensions and color.
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    draw_side(width, height)
    t.end_fill()
    center_x = x + width / 2
    center_y = y - height / 2
    return center_x, center_y
# Draw a circle with the specified center, radius, and color.
def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
# Draw a flagpole with the specified coordinates, height, and color.
def draw_flagpole(x, y, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.pensize(5)
    t.setheading(90)
    t.forward(height)
    t.pensize(1)
# Draw a flag with a flagpole, a rectangular flag, and a circle on the flag.
def draw_flag(x, y, scale_factor):
    flagpole_height = 200 * scale_factor
    flag_width = 300 * scale_factor
    flag_height = 150 * scale_factor
    circle_radius = 50 * scale_factor

    
    draw_flagpole(x, y, flagpole_height, "black")

   
    rect_x = x
    rect_y = y + flagpole_height
    center_x, center_y = draw_rectangle(rect_x, rect_y, flag_width, flag_height, "blue")

    
    circle_x = center_x
    circle_y = center_y + flag_height / 2
    draw_circle(circle_x, circle_y + 120, circle_radius, "red")
# Draw a flag with a flagpole, a rectangular flag, and a circle on the flag.
def main():
    t.speed(0)
    t.bgcolor("white")
    draw_flag(-200, -100, 1)
    draw_flag(100, -100, 0.5)
    t.hideturtle()
    t.done()
main()