def print_ascii_codes(s):
    for char in s:
        print(f"'{char}' : {ord(char)}")

sample_string = "Akhliddin"
print_ascii_codes(sample_string)