import turtle

# Function to get color from a character without using a dictionary
def get_color(character):
    if character == '0':
        return 'black'
    elif character == '1':
        return 'white'
    elif character == '2':
        return 'red'
    elif character == '3':
        return 'blue'
    elif character == '4':
        return 'yellow'
    elif character == '5':
        return 'green'
    elif character == '6':
        return 'orange'
    elif character == '7':
        return 'purple'
    else:
        return None

# Function to draw a colored pixel using Turtle
def draw_color_pixel(color_string, turta):
    turta.fillcolor(color_string)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(20)
        turta.left(90)
    turta.end_fill()

# Function to draw a pixel based on color_string using draw_color_pixel
def draw_pixel(color_string, turta):
    color = get_color(color_string)
    if color is not None:
        draw_color_pixel(color, turta)
    else:
        print(f"Character '{color_string}' does not have a corresponding color.")

# Function to draw a line from a string
def draw_line_from_string(color_string, turta):
    for character in color_string:
        color = get_color(character)
        if color is not None:
            # Draw the pixel and move to the next position
            draw_pixel(character, turta)
            turta.penup()
            turta.forward(20)  # Move to the right by 20 units after each pixel (no gap)
            turta.pendown()
        else:
            # If an invalid color is encountered, return False
            print(f"Invalid color character '{character}' encountered.")
            return False
    return True

# New function to continuously draw pixels in the same row based on user input
def draw_shape_from_string(turta):
    turta.penup()  # Ensure the turtle doesn't draw lines between pixels
    
    # Set fixed starting position at the top of the screen
    start_x, start_y = -200, 250  # Starting near the top with specific coordinates
    turta.goto(start_x, start_y)  # Move to the specified starting position
    
    while True:
        # Prompt the user for input
        color_string = input("Enter a string of color codes (0-7), or press enter to stop: ")
        
        # If the user enters an empty string, break the loop and stop
        if color_string == "":
            print("Empty input, stopping the drawing.")
            break
        
        # Call draw_line_from_string to draw the row
        is_valid = draw_line_from_string(color_string, turta)
        
        # If the string contains an invalid color, stop drawing
        if not is_valid:
            print("Invalid color encountered, stopping the drawing.")
            break


# Setup the Turtle environment
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("white")

# Create a turtle object
turta = turtle.Turtle()
turta.speed(0)  # Set turtle speed to maximum for faster drawing

# Call the function to start drawing based on user input
draw_shape_from_string(turta)

# End the turtle drawing
turtle.done()
