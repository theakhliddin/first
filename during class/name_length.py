def count_letters(name):
    return len(name)

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(f"The number of letters in your name is: {count_letters(name)}")

lando = name
a = lando[0]
b = lando[5]
c = lando[30]
d = lando[-1]
e = lando[-10]
f = lando[-11]
print(a, b, c, d, e, f)