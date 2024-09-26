"""
GCIS-123 Class Activity & Problem Solving #1 Turtle Scenery
This program draws a customizable scene with a table, layered cake, candle, and decoration.
"""

import turtle

def setup_screen():
    """Set up the turtle screen with a title and background color."""
    screen = turtle.Screen()
    screen.title("GCIS-123 Turtle Scenery")
    screen.setup(400, 300)
    screen.bgcolor("skyblue")
    return screen

def create_turtle():
    """Create and configure a turtle object for drawing."""
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.hideturtle()
    return t

def draw_rectangle(t, width, height, color):
    """Draw a filled rectangle."""
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_table(t, x, y, width, height, color):
    """Draw a table at the specified position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_rectangle(t, width, height, color)

def draw_cake_layer(t, width, height, color):
    """Draw a single cake layer."""
    draw_rectangle(t, width, height, color)

def draw_cake(t, x, y, width, layers, colors):
    """Draw a layered cake."""
    layer_height = 30
    for i, color in enumerate(colors):
        t.penup()
        t.goto(x, y + i * layer_height)
        t.pendown()
        draw_cake_layer(t, width, layer_height, color)

def draw_candle(t, x, y, height, color):
    """Draw a candle on the cake."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_rectangle(t, 10, height, color)
    # Draw flame
    t.penup()
    t.goto(x + 5, y + height)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

def draw_star(t, x, y, size):
    """Draw a star decoration."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def get_user_input():
    """Get user input for customizing the scene."""
    table_color = input("Enter table color: ")
    cake_layers = int(input("Enter number of cake layers (1-5): "))
    cake_colors = []
    for i in range(cake_layers):
        color = input(f"Enter color for cake layer {i+1}: ")
        cake_colors.append(color)
    candle_color = input("Enter candle color: ")
    return table_color, cake_layers, cake_colors, candle_color

def draw_scene(screen, t, table_color, cake_layers, cake_colors, candle_color):
    """Draw the entire scene based on user input."""
    # Draw table
    draw_table(t, -100, -120, 200, 20, table_color)
    
    # Draw cake
    draw_cake(t, -75, -100, 150, cake_layers, cake_colors)
    
    # Draw candle
    draw_candle(t, 0, -100 + (30 * cake_layers), 40, candle_color)
    
    # Draw star decoration
    draw_star(t, 100, 100, 20)
    
    # Display the drawing
    screen.exitonclick()

def main():
    """Main function to set up the scene and draw based on user input."""
    screen = setup_screen()
    t = create_turtle()
    
    table_color, cake_layers, cake_colors, candle_color = get_user_input()
    
    draw_scene(screen, t, table_color, cake_layers, cake_colors, candle_color)

if __name__ == "__main__":
    main()