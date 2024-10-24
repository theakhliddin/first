import turtle


def draw_shape(turta, shape_description):
   
    """Takes a turtle object and a description of a shape, validates it,
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
        with open(file_path, 'r') as file:
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

def main():
    draw_shape()
    draw_shape_from_file()
