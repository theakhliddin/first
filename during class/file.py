def print_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line, end = '')

print_lines(r"during class\\hello.txt")