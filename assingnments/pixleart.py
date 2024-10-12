import turtle as t



def draw_shape_from_file(turta):
    """
    Prompts the user for a text file path, reads its content, and uses
    the draw_shape function to generate an image.
    """
    # Prompt user for file path and remove surrounding whitespace
    file_path = input("Enter the path of the .txt file containing shape data: ").strip()

    # Check if the file has a valid '.txt' extension
    if not file_path.lower().endswith('.txt'):
        print("Error: Please provide a valid '.txt' file.")
        return

    try:
        # Open and read the content of the file
        with open("first//assingnments//drawing01.txt", 'r') as file:
            shape_data = file.read().strip()

        # Check if the file is empty
        if not shape_data:
            print("Error: The file is empty. Please provide a valid shape definition.")
            return

        # Use the draw_shape function to draw the shape based on the file content
        draw_shape(turta, shape_data)
        print("Shape successfully drawn from the file!")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# Assuming `turta` is your turtle object and `draw_shape_from_file` is properly defined:
# draw_shape_from_file(turta)




# Function to get color from a character without using a dictionary
def get_color(character):
    if character == '0':
        return 'black'
    elif character == '1':
        return 'white'
    elif character == '2':
        return 'red'
    elif character == '3':
        return 'yellow'
    elif character == '4':
        return 'orange'
    elif character == '5':
        return 'green'
    elif character == '6':
        return 'yellowgreen'
    elif character == '7':
        return 'sienna'
    elif character == '8':
        return 'tan'
    elif character == '9':
        return 'gray'
    elif character == 'A':
        return 'darkgray'
    else:
        return None

# Function to draw a colored pixel using Turtle
def draw_color_pixel(color_string, turta):
    t.fillcolor(color_string)
    t.begin_fill()
    for _ in range(4):
        t.forward(turta)
        t.left(90)
    t.end_fill()

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
            t.penup()
            t.forward(turta)  # Move to the right by 20 units after each pixel (no gap)
            t.pendown()
        else:
            # If an invalid color is encountered, return False
            print(f"Invalid color character '{character}' encountered.")
            return False
    return True

# New function to continuously draw pixels in the same row based on user input
def draw_shape_from_string(turta):
    '''t.penup()'''  # Ensure the turtle doesn't draw lines between pixels
    
    # Set fixed starting position at the top of the screen
    start_y=turta

      # Move to the specified starting position
    
    while True:
        # Prompt the user for input
        color_string = input("Enter a string of color codes (0-9 or capital A), or press enter to stop: ")
        
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
        t.penup()
        t.goto(0,-start_y)
        t.pendown()
        start_y=start_y+turta

#This will help to draw a grid using red and black 
def draw_grid(turta):
    grid1='02020202020202020202' #0 is black and 2 is red 
    grid2='20202020202020202020'
    start_y=turta
    for i in range(1,21):
        if i% 2 == 0: #we gave a condition saying if i is an even number use grid2 orelse use grid 1 (basically being odd)
            draw_line_from_string(grid2,turta)
        else:
            draw_line_from_string(grid1,turta)
        t.penup()  
        t.goto(0,-start_y)#These are to chnage lines from one row to another and go down
        t.pendown()
        start_y=start_y+turta


def draw_shape(turta, shape_description):
    """
    Takes a turtle object and a description of a shape, validates it,
    and then draws the corresponding shape.
    """
    # Validate the shape description (this could be improved depending on the expected format)
    if not isinstance(shape_description, str) or not shape_description.strip():
        print("Error: Invalid shape description provided.")
        return

    # Assume the shape description is valid and draw the shape
    # You can add more complex parsing logic for shape data here
    try:
        # Placeholder: This is where the actual drawing logic goes
        # For example, the shape_description might be a set of commands to draw
        print(f"Drawing shape based on description: {shape_description}")
        # Here, you would have the code that uses the `turta` object to draw the shape
        # Example: `turta.forward(100)`, `turta.circle(50)` based on the description
        # draw_shape_from_description(turta, shape_description) <-- complex logic here
        
    except Exception as e:
        print(f"An error occurred while drawing the shape: {e}")



# Create a turtle object
t.speed(0)  # Set turtle speed to maximum for faster drawing
draw_grid(20)
# End the turtle drawing
t.done()


def main():
    draw_shape_from_file()
    draw_color_pixel()
    draw_line_from_string()