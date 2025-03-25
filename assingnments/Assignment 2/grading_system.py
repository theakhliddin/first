import csv, re

"""
This script imports csv and re(regular expressions)

This script uses incremental development for its function, so it can generate the appropiate
grades representing the student's score from reading the provided csv.file.
Additonally is able to calculate the class average, and count the numbers of failing students.
functions posses error handlingscx

Functions:
calculate_grade()  # This function represent score values with the appropiate letter grade

process_students() # This function will process reading the student grade from a csv and calling calculate_grade() to represent the students name with their grade

calculate_average_grade() # This function will calculate the average of the class by reading the csv file and calling calculate_grade()

count_failing_students() # This function counts failing students by reading the csv file and finding digits using regular expressions that cover the range from 0 - 59 to represent those scores with the grade 'F'

main() # The main function that will be called to start the script and has exception handling allowing the user to retry inputting a valid file. 

It calls the functions:
process_students()
calculcate_average_grade()
count_failing_students()
"""

# Function to represent score values as letter grade
def calculate_grade(score): 
    """
    Uses 'if' to set conditions that represent scores with appropiate letter grade
    """

    # Setting conditions using if statement to represent score with letter grade
    if score < 0 or score > 100: # Incase if values were out of range
        return "Error: Score is out of valid range!"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Function to process the students' grades
def process_students(filename): 
    """
    Reads the student's grade from the csv file,
    and then uses the function calculate_grade() to represent the students grade along with their name.
    Handles errors regarding file handling and value errors seperately
    """
    # This 'try' is for handling FileNotFoundError exceptions
    try:
        # Opens the file and reads it
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                try: # This 'try' is for handling ValueError exceptions
                    name, score = row # Stores the values from row in the format of name, score
                    score = float(score) # Casts the score into a float
                    if score < 0 or score > 100:  # 'if' conditions incase for values out of range
                        print(f"Error: Invalid score for {name}")
                    else:
                        grade = calculate_grade(score)  # grade is the stored value after the function represents score values into letters
                        print(f"{name}: {grade}")
                except ValueError: # If the score was Non-numeric
                    print(f"Error: Non-numeric score for {row[0]}")
    except FileNotFoundError: # If the file was not found or valid
        print(f"Error: The file '{filename}' was not found!")  
        raise # Raises the error so it can be caught in the main(), so it can work accordingly

# Function to calculate the average grade of the class
def calculate_average_grade(filename):
    """
    Calculates and prints the average of the class by reading the csv file by rows
    and calculations that involve using the function 'calculate_grade()'.
    Handles ValueErrors and FileNotFoundError seperately
    """
    
    total_score = 0  # Initializes the total score
    total_students = 0  # Initializes the total number of students

    try: # This 'try' is for handling FileNotFoundError exceptions
        with open(filename, 'r') as file: # Opens the file and reads it using a loop
            csv_reader = csv.reader(file)
            for row in csv_reader:
                try:  # This 'try' is for handling ValueError exceptions
                    score = float(row[1]) 
                    total_score += score
                    total_students += 1 # To shift through rows in the csv
                except ValueError:  # If the score is not a number
                    print("Invalid score found in the file!")
    except FileNotFoundError:  # If the file is not found
        print(f"File '{filename}' not found!")
        return

    if total_students > 0:  # Checks if there are students in the class
        average_score = total_score / total_students  # Calculates the average score
        average_grade = calculate_grade(average_score)  # Calculates the average grade
        print(f"Class Average: {average_grade}")  # Prints the average grade
    else:
        print("Error: Invalid student data")


def count_failing_students(filename):
    """
    Counts the amount of failing students in class by reading the csv,
    and using regular expressions to find values from 0 - 59 and representing scores with those values as 'F'.
    Handles FileNotFoundError's
    """

    try: 
        failing_count = 0 # Setting up a counter

        with open(filename, 'r') as file: # To read the csv
            content = file.read()

            failing_grades = re.findall(r'[0-5][0-9]', content) # Using regular expressions to find the values that match with the regex, and storing them in content
            failing_count = len(failing_grades) # Stored value from reading falling_grades

        print(f"Number of Failing Students: {failing_count}")

    except FileNotFoundError: # If the file was not found
        print(f"The file {filename} was not found") 

# Main function to call
def main():
    """
    Prompts the user to input a filename and retrys if it was invalid.
    Calls the needed functions to output printing out student names with their grades,
    the class average, and the number of failing students.
    """
    while True: 
        filename = input("Enter the filename: ") # Ask user to input the file name and retrys if incorrect via while loop
        try:
            process_students(filename)  # Calls the function to process the students' grades
            calculate_average_grade(filename)  # Calls the function to calculate the average grade
            count_failing_students(filename)  # Calls the function to count failing students
            break  

        # Exceptions to catch errors
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found! Try again.")
        except:  
            print("Try again with a valid filename.")

main() # Calls main
