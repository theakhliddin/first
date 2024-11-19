def ascii_codes(a_string):
    for char in a_string:
        print(f"{char}: {ord(char)}")

def decode_ascii(ascii_codes):
    decoded_string = ""
    for code in ascii_codes:
        decoded_string += chr(code)
    return decoded_string

def main():
    test_string = "SWEC-123"  
    ascii_codes(test_string)
    ascii_code_list = [83, 87, 69, 67, 45, 49, 50, 51]
    decoded_string = decode_ascii(ascii_code_list)
    print("Decoded string:", decoded_string)

main()