import re

def find_digits(a_str):
    for match in re.findall("[0-9]+", a_str):
        print(match)
find_digits("abcd345efgh90")