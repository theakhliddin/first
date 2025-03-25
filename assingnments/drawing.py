# drawing.py
import turtle
# Importing relevant functions from pixart.py
from pixleart import draw_shape_from_file

def main():
    """
    Main function to prompt the user for input and call the drawing function.
    """
    try:
        # Assume `turta` is an object for drawing (e.g., a turtle object)
        # This should be set up properly in your real environment
        turta = None  # Placeholder for the turtle object setup

        # Prompt the user for the path to the text file
        file_path = input("Enter the path of the .txt file containing shape data: ").strip()

        # Call the draw_shape_from_file function
        draw_shape_from_file(turta, file_path)
        print("Shape successfully drawn from the file!")

    except Exception as e:
        print(f"An error occurred: {e}")

# This ensures that the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()