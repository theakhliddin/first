import turtle

# Setup turtle window
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Birthday Cake Drawing")

# Create turtle object
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Function to draw a rectangle
def draw_rectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw the table legs
def draw_leg(x, y, leg_width, leg_height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_rectangle(t, leg_width, leg_height, color)

# Function to draw the cake with layers and some decoration
def draw_cake():
    # Base layer (Table)
    t.penup()
    t.goto(-150, -150)
    t.pendown()
    draw_rectangle(t, 300, 50, "white")  # table

    # Draw four legs for the table
    leg_width = 20
    leg_height = 100
    leg_color = "brown"

    # Front left leg
    draw_leg(-150, -250, leg_width, leg_height, leg_color)
    # Front right leg
    draw_leg(130, -250, leg_width, leg_height, leg_color)
    # Back left leg
    draw_leg(-130, -250, leg_width, leg_height, leg_color)
    # Back right leg
    draw_leg(110, -250, leg_width, leg_height, leg_color)

    # Bottom cake layer
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    draw_rectangle(t, 200, 100, "yellow")  # bottom layer

    # Frosting for bottom layer
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    draw_rectangle(t, 200, 10, "white")

    # Middle cake layer
    t.penup()
    t.goto(-80, 10)
    t.pendown()
    draw_rectangle(t, 160, 60, "pink")  # middle layer

    # Frosting for the middle layer
    t.penup()
    t.goto(-80, 70)
    t.pendown()
    draw_rectangle(t, 160, 10, "white")

    # Top cake layer
    t.penup()
    t.goto(-60, 80)
    t.pendown()
    draw_rectangle(t, 120, 40, "lightyellow")  # top layer

    # Frosting for top layer
    t.penup()
    t.goto(-60, 120)
    t.pendown()
    draw_rectangle(t, 120, 10, "white")

# Function to draw candles
def draw_candle(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)  # Ensure turtle is facing right direction
    t.pendown()
    t.fillcolor("white")

    # Draw candle body
    t.begin_fill()
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(10)
    t.end_fill()

    # Draw flame
    t.penup()
    t.goto(x + 5, y + 40)  # Position above the candle
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

# Function to add candles on the top layer of the cake
def add_candles():
    candle_positions = [-50, -20, 10, 40]  # x positions for candles
    for pos in candle_positions:
        draw_candle(pos, 120)

# Drawing the cake and candles
draw_cake()
add_candles()

# Hide the turtle and complete
t.hideturtle()
screen.mainloop()
