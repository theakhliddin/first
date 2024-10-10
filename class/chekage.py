def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
        raise  ValueError("You must be at least 18 years old")
    else:
        return "Age is valid. You are allowed to proceed"

def get_user_input():
    while True:
        try:
            age = int(input("Please enter your age: "))
            return age
        except  ValueError:
            print("Invalid input. Please enter a valid age")

def main():
    try:
        user_age = get_user_input()
        
        message = check_age(user_age)
        print(message)
        
    except  ValueError as e:
        print(f"Error: {e}")
    
if __name__  == "__main__":
    main()



