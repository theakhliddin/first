import pytest
from grading_system import calculate_grade, process_students, calculate_average_grade, count_failing_students

"""
Imports pytest, and the functions from the main script
This is a script to be used to test the functions from the main script,
and checks if the code passes the cases.

Functions to be tested:

calculate_grade() for 3 cases

process_students() 1 case

calculate_average_grade() 1 case

count_failing_students() 1 case

"""

# Testing cases for caculate_grade()
def test_caculate_grade():
    """
    It test 3 cases for calculate_grade() and checks if it passes them
    """
    # Case 1: Testing for a negative value
    assert calculate_grade(-5) == "Error: Score is out of valid range!"
    
    # Case 2: Testing for a boundary value
    assert calculate_grade(90) == "A"

    # Case 3: Testing for a valid in-range value
    assert calculate_grade(75) == "C"



# Testing a case for process_students()
def test_process_students_file():
    """
    Checks for the case, if an invalid file was inputted
    """
    # Testing if it still passes after inputting a invalid file
    try:
         process_students("a_file_that_does_not_exist")
    except Exception as error:
        assert str(error) == "Error: The file 'a_file_that_does_not_exist' was not found!"

# Testing a case for calculate_average_grade()
def test_calculate_average_grade():
    """
    Checks for the case if there was an error during calculations caused by invalid data
    """
    # Testing if it passes properly during the run of the function, and asserting an exception incase of an error
    try:
        calculate_average_grade("student.csv")
    except:
        assert False, "There was an error while calculating the average"


# Testing a case for count_failing_students()
def test_count_failing_students():
    """
    Checks for the case if there was an error during calculations caused by invalid data
    """
    # Testing if it passes properly during the run of the funtion, and asserting an exception incase of an error
    try:
        count_failing_students("student.csv")
    except:
        assert False, "There was an error while counting failing students"



# To make sure to run the script properly for pytesting
if __name__ == "__main__":
    pytest.main()