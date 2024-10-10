def sum_int_from_line(file_path):
    try:
        with open("first/class/any2.txt", 'r') as file:
            total_sum = sum(int(num) for line in file for num in line.split())
        
        print(f"The sum of all integers is: {total_sum}")
        
    except(ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

sum_int_from_line("first/class/any2.txt")