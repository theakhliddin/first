def draw_shape_from_file(turta):
    file_path = input("Enter the path of the file that you want to read its content: ")

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        turta.draw_shape_from_string(content)
        print(f"The shape from {file_path} has been drawn successfully.")
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

draw_shape_from_file()