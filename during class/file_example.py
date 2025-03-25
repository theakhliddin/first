file = open(r"during class\\hello.txt")
for line in file:
    length = len(line)
    print(length)
file.close()