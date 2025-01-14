import random
import string

def generate_password():
    length = int(input("Enter the password length: "))
    include_digits = input("Include digits? (yes/no): ").lower() == "yes"
    include_symbols = input("Include symbols? (yes/no): ").lower() == "yes"
    
    
    chars = string.ascii_letters # A-Z, a-z
    if include_digits:
        chars += string.digits #add 0-9
    if  include_symbols:
        chars += string.punctuation #add !, @, #, $, etc.


    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated password : {password}")
generate_password()