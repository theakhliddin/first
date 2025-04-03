tupa = (1, 2, 3, 4)
print(tupa)
tupb = ('f', 5, False, 6.14)
print(tupb)
tupc = tuple("abcdefghijklmnopqrstuvwxyz")
print(tupc)
lista = [1, 2, 3, 4]
print(lista)
listb = ['f', 5, False, 6.14]
print(listb)
listc = list("abcdefghijklmnopqrstuvwxyz")
print(listc)
listb += listc
print(listb)

def cat():
    """
    Concatenates two tuples and returns the result.
    """
    tup1 = (1, 2, 3)
    tup2 = (4, 5, 6)
    print(tup1 + tup2)

def main():
    cat()
main()