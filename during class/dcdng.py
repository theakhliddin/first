def decode(encoded_message):
    
    numbers = encoded_message.split()
    
    
    decoded_chars = [chr(int(num)) for num in numbers]
    

    decoded_message = ''.join(decoded_chars)
    
    return decoded_message

encoded_message = "66 101 32 115 117 114 101 32 116 111 32 100 114 105 110 107 32 121 111 117 114 32 79 118 97 108 116 105 110 101 46"
print(decode(encoded_message))