def login():
    while True:
        userid = input("Enter your user id: ")
        password = input("Enter your password: ")
        try:
            validate(userid, password)
        except ValueError as ve:
            attempts -= 1
            if attempts > 0:
                print("Invalid" ,attempts, "Please try again.")
            else:
                raise ve
login()