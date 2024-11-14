# Function to assign grade based on marks
def assignGrade(marks):
    if marks >= 90:
        return "Student got: A"
    elif marks >= 80:
        return "Student got: B"
    elif marks >= 70:
        return "Student got: C"
    elif marks >= 60:
        return "Student got: D"
    else:
        return "Failed"

# Main function to prompt user for marks and get the grade
def main():
    # Prompt the user to enter the marks
    student_marks = int(input("Enter the student's marks: "))
    
    # Call the function and get the grade
    grade = assignGrade(student_marks)
    
    # Display the assigned grade
    print(f"The student's grade is: {grade}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
